#!/usr/bin/env python3
"""Build a static browsing site for bxs-awesome-skills."""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
ASSETS_DIR = ROOT / "site-assets"
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
CODE_BLOCK_RE = re.compile(r"```([a-zA-Z0-9_-]*)\n(.*?)```", re.S)

STATUS_LABELS = {
    "candidate": "候选",
    "under_review": "待复审",
    "verified": "已验证",
    "deprecated": "已弃用",
    "archived": "已归档",
}
INSTALL_LABELS = {"low": "低", "medium": "中", "high": "高"}
SECURITY_NOTES = {
    "A": "低风险，边界清晰，可优先考虑。",
    "B": "风险可控，安装前仍需核对依赖与权限。",
    "C": "有明显风险点，建议先看审计与上游。",
    "D": "信任信号不足，默认不推荐安装。",
}
COMPATIBILITY_UI_LABELS = {"native": "原生", "compatible": "兼容"}
TOOL_LABELS = {
    "claude-code": "Claude Code",
    "openai-agents": "OpenAI Agents",
    "gemini-cli": "Gemini CLI",
    "openclaw": "OpenClaw",
}
VERDICT_LABELS = {
    "recommended": "推荐安装",
    "conditional": "按场景安装",
    "caution": "暂缓安装",
}


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def split_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text
    front_matter = yaml.safe_load(match.group(1)) or {}
    return front_matter, match.group(2).strip()


def parse_sections(body: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    buffer: list[str] = []

    for line in body.splitlines():
        if line.startswith("## "):
            if current is not None:
                sections[current] = "\n".join(buffer).strip()
            current = line[3:].strip()
            buffer = []
            continue
        if current is not None:
            buffer.append(line)

    if current is not None:
        sections[current] = "\n".join(buffer).strip()

    return {key: value for key, value in sections.items() if value}


def render_inline(text: str) -> str:
    placeholders: dict[str, str] = {}

    def stash(value: str) -> str:
        token = f"TOKEN{len(placeholders)}PLACEHOLDER"
        placeholders[token] = value
        return token

    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: stash(
            f'<a href="{html.escape(m.group(2), quote=True)}">{html.escape(m.group(1))}</a>'
        ),
        text,
    )
    text = re.sub(
        r"`([^`]+)`",
        lambda m: stash(f"<code>{html.escape(m.group(1))}</code>"),
        text,
    )
    text = re.sub(
        r"\*\*([^*]+)\*\*",
        lambda m: stash(f"<strong>{html.escape(m.group(1))}</strong>"),
        text,
    )
    escaped = html.escape(text)
    for token, value in placeholders.items():
        escaped = escaped.replace(token, value)
    return escaped


def parse_bullets(content: str) -> list[str]:
    return [line.strip()[2:].strip() for line in content.splitlines() if line.strip().startswith("- ")]


def parse_numbered(content: str) -> list[str]:
    items: list[str] = []
    for line in content.splitlines():
        match = re.match(r"\d+\.\s+(.*)", line.strip())
        if match:
            items.append(match.group(1).strip())
    return items


def parse_key_values(content: str) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            stripped = stripped[2:].strip()
        if not stripped:
            continue
        match = re.match(r"([^：:]+)[：:]\s*(.+)", stripped)
        if match:
            items.append((match.group(1).strip(), match.group(2).strip()))
    return items


def parse_code_blocks(content: str) -> list[dict[str, str]]:
    examples: list[dict[str, str]] = []
    last_end = 0
    for idx, match in enumerate(CODE_BLOCK_RE.finditer(content), start=1):
        prefix = content[last_end:match.start()].strip()
        lines = [line.strip() for line in prefix.splitlines() if line.strip()]
        label = lines[-1].rstrip("：:") if lines else f"示例 {idx}"
        note = " ".join(lines[:-1]) if len(lines) > 1 else ""
        examples.append(
            {
                "label": label,
                "note": note,
                "lang": match.group(1) or "text",
                "code": match.group(2).strip(),
            }
        )
        last_end = match.end()
    return examples


def date_label(value: Any) -> str:
    if value in (None, "", "null"):
        return "未记录"
    if hasattr(value, "strftime"):
        return value.strftime("%Y-%m-%d")
    text = str(value)
    if "T" in text:
        return text.split("T", 1)[0]
    if " " in text:
        return text.split(" ", 1)[0]
    return text


def compute_verdict(skill: dict[str, Any]) -> tuple[str, str]:
    status = skill["status"]
    security = skill["security_grade"]
    quality = int(skill.get("quality_score", 0))

    if status == "verified" and security in {"A", "B"} and quality >= 75:
        return "recommended", "已验证，价值与可信度信号较强。"
    if security in {"A", "B"} and status in {"verified", "under_review", "candidate"}:
        return "conditional", "可按场景安装，但应先确认依赖、权限和边界。"
    return "caution", "信任或验证信号不足，建议先看审计、上游和评论。"


def source_summary(skill: dict[str, Any], skill_json: dict[str, Any]) -> tuple[str, str]:
    source_type = skill.get("source_type", "local")
    source_url = skill.get("source_url")
    if not source_url:
        source = skill_json.get("source", {})
        source_url = source.get("upstream") or source.get("url")

    if source_type == "local" and source_url:
        return "本地收录 / 有公开上游", str(source_url)
    if source_type == "local":
        return "本地收录 / 无公开上游", ""
    if source_url:
        return "外部技能 / 有公开来源", str(source_url)
    return "外部技能", ""


def load_comments() -> dict[str, list[dict[str, Any]]]:
    comments: dict[str, list[dict[str, Any]]] = {}
    for path in sorted((ROOT / "comments").glob("*.yaml")):
        payload = load_yaml(path) or {}
        comments[payload.get("skill_slug", path.stem)] = payload.get("comments", []) or []
    return comments


def load_skill_json(slug: str) -> dict[str, Any]:
    path = ROOT / "skills" / slug / "skill.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_install_examples(examples: list[dict[str, str]]) -> list[dict[str, str]]:
    labels = ["安装", "验证", "补充"]
    normalized: list[dict[str, str]] = []
    for idx, item in enumerate(examples):
        label = item["label"]
        if label.startswith("示例 ") and idx < len(labels):
            label = labels[idx]
        normalized.append({**item, "label": label})
    return normalized


def compatibility_list(skill_json: dict[str, Any]) -> list[dict[str, str]]:
    items = []
    for tool, state in (skill_json.get("compatibility") or {}).items():
        items.append({"name": TOOL_LABELS.get(tool, tool), "state": state})
    return items


def build_skill_payload(skill: dict[str, Any], comments_map: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    slug = skill["slug"]
    readme_path = ROOT / skill["profile_path"]
    _, body = split_front_matter(readme_path)
    sections = parse_sections(body)
    skill_json = load_skill_json(slug)
    verdict, verdict_note = compute_verdict(skill)
    source_label, source_url = source_summary(skill, skill_json)
    comments = comments_map.get(slug, [])
    search_parts = [
        skill["name"]["zh"],
        skill.get("name", {}).get("en", ""),
        skill["summary"]["zh"],
        " ".join(skill.get("tags", [])),
        " ".join(skill.get("category", [])),
        " ".join(parse_bullets(sections.get("适合场景", ""))),
    ]

    return {
        "slug": slug,
        "name": skill["name"]["zh"],
        "name_en": skill.get("name", {}).get("en", ""),
        "summary": skill["summary"]["zh"],
        "categories": skill.get("category", []),
        "tags": skill.get("tags", []),
        "status": skill["status"],
        "status_label": STATUS_LABELS.get(skill["status"], skill["status"]),
        "install_complexity": skill["install_complexity"],
        "install_label": INSTALL_LABELS.get(skill["install_complexity"], skill["install_complexity"]),
        "quality_score": skill.get("quality_score", 0),
        "security_grade": skill["security_grade"],
        "security_score": skill.get("security_score", 0),
        "security_note": SECURITY_NOTES.get(skill["security_grade"], ""),
        "maintainer": skill.get("maintainer") or skill_json.get("quality", {}).get("maintainer", "未记录"),
        "last_verified_at": date_label(skill.get("last_verified_at") or skill_json.get("quality", {}).get("last_verified_at")),
        "verdict": verdict,
        "verdict_label": VERDICT_LABELS[verdict],
        "verdict_note": verdict_note,
        "source_type": skill.get("source_type", "local"),
        "source_label": source_label,
        "source_url": source_url,
        "fit": parse_bullets(sections.get("适合场景", "")),
        "quick_checks": parse_bullets(sections.get("快速判断", "")),
        "value": parse_numbered(sections.get("核心价值", "")),
        "install_steps": normalize_install_examples(parse_code_blocks(sections.get("最小上手", ""))),
        "usage_examples": parse_code_blocks(sections.get("使用示例", "")),
        "boundaries": parse_key_values(sections.get("依赖与边界", "")),
        "trust": parse_key_values(sections.get("信任与维护", "")),
        "review_notes": parse_bullets(sections.get("审核与反馈", "")),
        "compatibility": compatibility_list(skill_json),
        "comments": comments,
        "comment_count": len(comments),
        "detail_url": f"/skills/{slug}/",
        "data_url": f"/data/skills/{slug}.json",
        "search_blob": " ".join(part for part in search_parts if part).lower(),
    }


def render_list(items: list[str], ordered: bool = False, css_class: str = "panel-list") -> str:
    if not items:
        return '<p class="muted">暂无补充信息。</p>'
    tag = "ol" if ordered else "ul"
    return f'<{tag} class="{css_class}">' + "".join(
        f"<li>{render_inline(item)}</li>" for item in items
    ) + f"</{tag}>"


def render_key_values(items: list[tuple[str, str]]) -> str:
    if not items:
        return '<p class="muted">暂无补充信息。</p>'
    blocks = []
    for key, value in items:
        blocks.append(
            "<div>"
            f"<dt>{render_inline(key)}</dt>"
            f"<dd>{render_inline(value)}</dd>"
            "</div>"
        )
    return '<dl class="kv-grid">' + "".join(blocks) + "</dl>"


def render_examples(items: list[dict[str, str]]) -> str:
    if not items:
        return '<p class="muted">暂无示例。</p>'
    blocks = []
    for item in items:
        note = f"<p class=\"small\">{render_inline(item['note'])}</p>" if item["note"] else ""
        blocks.append(
            '<article class="example-card">'
            '<header>'
            f"<strong>{render_inline(item['label'])}</strong>"
            f"<span>{html.escape(item['lang'])}</span>"
            "</header>"
            f"{note}"
            f"<pre><code>{html.escape(item['code'])}</code></pre>"
            "</article>"
        )
    return '<div class="example-stack">' + "".join(blocks) + "</div>"


def render_compatibility(items: list[dict[str, str]]) -> str:
    if not items:
        return '<p class="muted">未声明兼容性。</p>'
    return '<div class="compatibility-row">' + "".join(
        f'<span class="compatibility-chip compatibility-chip--{html.escape(item["state"])}">'
        f'{html.escape(item["name"])} · {html.escape(COMPATIBILITY_UI_LABELS.get(item["state"], item["state"]))}'
        '</span>'
        for item in items
    ) + '</div>'


def render_comments(items: list[dict[str, Any]]) -> str:
    if not items:
        return '<p class="muted">暂无已审核评论。</p>'
    blocks = []
    for item in items[:3]:
        meta = []
        if item.get("verdict"):
            meta.append(str(item["verdict"]))
        if item.get("rating"):
            meta.append(f'{item["rating"]}/5')
        blocks.append(
            '<article class="example-card">'
            '<header>'
            f"<strong>{render_inline(item.get('author', '匿名'))}</strong>"
            f"<span>{render_inline(' · '.join(meta) if meta else '已审核反馈')}</span>"
            '</header>'
            f"<p class=\"small\">{render_inline(item.get('content', ''))}</p>"
            '</article>'
        )
    return '<div class="example-stack">' + "".join(blocks) + "</div>"


def related_skills(current: dict[str, Any], skills: list[dict[str, Any]]) -> list[dict[str, Any]]:
    related: list[tuple[int, int, dict[str, Any]]] = []
    current_categories = set(current["categories"])
    current_tags = set(current["tags"])
    for candidate in skills:
        if candidate["slug"] == current["slug"]:
            continue
        score = len(current_categories & set(candidate["categories"])) * 10 + len(current_tags & set(candidate["tags"]))
        if score <= 0:
            continue
        rank = 0 if candidate["verdict"] == "recommended" else 1 if candidate["verdict"] == "conditional" else 2
        related.append((rank, -score, candidate))
    related.sort(key=lambda item: (item[0], item[1], -item[2]["quality_score"]))
    return [item[2] for item in related[:3]]


def top_examples(skills: list[dict[str, Any]], predicate) -> str:
    names = [f'<a href="{skill["detail_url"]}">{html.escape(skill["name"])}</a>' for skill in skills if predicate(skill)]
    if not names:
        return "暂无"
    return "、".join(names[:2])


def page_shell(title: str, description: str, body: str) -> str:
    return f"""<!doctype html>
<html lang=\"zh-CN\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>{html.escape(title)}</title>
  <meta name=\"description\" content=\"{html.escape(description)}\">
  <link rel=\"stylesheet\" href=\"/assets/site.css\">
</head>
<body>
{body}
<footer class=\"site-shell site-footer\">
  <p>bxs-awesome-skills · 面向人类浏览与 Agent 抓取的静态技能索引。</p>
</footer>
<script src=\"/assets/site.js\" defer></script>
</body>
</html>
"""


def render_topbar() -> str:
    return """
<header class="topbar">
  <div class="site-shell brand-row">
    <a class="brand" href="/">
      <span class="brand-mark">BXS</span>
      <span class="brand-copy">
        <strong>bxs-awesome-skills</strong>
        <span>先判断值不值得装，再决定怎么装</span>
      </span>
    </a>
    <nav class="nav-links">
      <a href="/#skills">技能索引</a>
      <a href="/#agent">Agent 数据</a>
      <a href="/data/skills.json">skills.json</a>
    </nav>
  </div>
</header>
"""


def render_home(skills: list[dict[str, Any]], categories: list[dict[str, Any]], updated_at: str) -> str:
    total = len(skills)
    recommended = [skill for skill in skills if skill["verdict"] == "recommended"]
    caution = [skill for skill in skills if skill["verdict"] == "caution"]
    low_install = [skill for skill in skills if skill["install_complexity"] == "low"]
    category_counts = {
        category["name"]["zh"]: sum(1 for skill in skills if category["name"]["zh"] in skill["categories"])
        for category in categories
    }

    quick_cards = [
        {
            "title": "推荐安装",
            "text": "已验证且安全信号较强，适合先看。",
            "metric": f"{len(recommended)} 个技能",
            "examples": top_examples(skills, lambda skill: skill["verdict"] == "recommended"),
        },
        {
            "title": "安装最轻",
            "text": "几乎不用额外准备，适合快速试用。",
            "metric": f"{len(low_install)} 个技能",
            "examples": top_examples(skills, lambda skill: skill["install_complexity"] == "low"),
        },
        {
            "title": "需要谨慎",
            "text": "信任或验证信号不足，先看边界再决定。",
            "metric": f"{len(caution)} 个技能",
            "examples": top_examples(skills, lambda skill: skill["verdict"] == "caution"),
        },
    ]

    quick_html = "".join(
        f'''<article class="quick-panel reveal">
  <h3>{html.escape(item["title"])}</h3>
  <p>{html.escape(item["text"])}</p>
  <p class="metric-line">{item["metric"]}</p>
  <p class="small">{item["examples"]}</p>
</article>'''
        for item in quick_cards
    )

    category_html = "".join(
        f'''<article class="category-card reveal">
  <h3>{html.escape(category["name"]["zh"])}</h3>
  <p>{html.escape(category["description"]["zh"])}</p>
  <p class="metric-line">{category_counts.get(category["name"]["zh"], 0)} 个技能</p>
  <button class="pill-button" data-category-jump="{html.escape(category["name"]["zh"])}">只看这一类</button>
</article>'''
        for category in categories
        if category_counts.get(category["name"]["zh"], 0)
    )

    cards_html = "".join(
        f'''<article class="skill-card reveal" data-skill-card data-search="{html.escape(skill["search_blob"])}" data-status="{html.escape(skill["status"])}" data-security="{html.escape(skill["security_grade"])}" data-install="{html.escape(skill["install_complexity"])}" data-source="{html.escape(skill["source_type"])}" data-verdict="{html.escape(skill["verdict"])}" data-category="{html.escape("|".join(skill["categories"]))}">
  <div class="card-head">
    <span class="verdict verdict--{html.escape(skill["verdict"])}">{html.escape(skill["verdict_label"])}</span>
    <span class="badge">{html.escape(skill["status_label"])}</span>
  </div>
  <h3><a href="{skill["detail_url"]}">{html.escape(skill["name"])}</a></h3>
  <p class="card-summary">{render_inline(skill["summary"])}</p>
  {render_list(skill["fit"][:2] or [skill["summary"]], css_class="card-list")}
  <div class="card-meta">
    <div><dt>来源</dt><dd>{render_inline(skill["source_label"])}</dd></div>
    <div><dt>安全</dt><dd>{html.escape(skill["security_grade"])} · {render_inline(skill["security_note"])}</dd></div>
    <div><dt>安装</dt><dd>{html.escape(skill["install_label"])}</dd></div>
    <div><dt>验证</dt><dd>{html.escape(skill["last_verified_at"])}</dd></div>
  </div>
  <div class="tag-list">{''.join(f'<span class="tag">{html.escape(tag)}</span>' for tag in skill["tags"][:4])}</div>
  <a class="card-link" href="{skill["detail_url"]}">查看详情</a>
</article>'''
        for skill in skills
    )

    category_options = "".join(
        f'<option value="{html.escape(category["name"]["zh"])}">{html.escape(category["name"]["zh"])}</option>'
        for category in categories
        if category_counts.get(category["name"]["zh"], 0)
    )

    agent_body = """
<ul class="agent-list">
  <li><code>/data/skills.json</code>：全量技能索引，适合检索和打分。</li>
  <li><code>/data/categories.json</code>：分类说明与排序。</li>
  <li><code>/data/skills/&lt;slug&gt;.json</code>：单技能详情，适合 Agent 精读。</li>
  <li>Cloudflare Pages 构建命令：<code>python3 scripts/build_site.py</code>，输出目录：<code>dist</code>。</li>
</ul>
"""

    return page_shell(
        "bxs-awesome-skills",
        "按任务、可信度和上手成本查找技能。",
        f"""
{render_topbar()}
<section class="hero">
  <div class="site-shell hero-grid">
    <div class="hero-panel reveal">
      <p class="eyebrow">Curated Skill Registry</p>
      <h1>先找到对的技能，再决定要不要装。</h1>
      <p class="lede">按任务、可信度和上手成本筛选。人类可以直接浏览，Agent 可以直接抓取稳定 JSON。</p>
      <div class="hero-actions">
        <a class="btn" href="#skills">开始找技能</a>
        <a class="btn-ghost" href="/data/skills.json">查看 skills.json</a>
      </div>
      <div class="hero-stats">
        <div class="stat-box"><span>已收录技能</span><strong>{total}</strong></div>
        <div class="stat-box"><span>推荐安装</span><strong>{len(recommended)}</strong></div>
        <div class="stat-box"><span>需谨慎</span><strong>{len(caution)}</strong></div>
        <div class="stat-box"><span>索引更新</span><strong>{html.escape(updated_at)}</strong></div>
      </div>
    </div>
    <aside class="trust-panel reveal">
      <span class="verdict verdict--recommended">三步判断</span>
      <p class="small">1. 先看是否 <code>verified</code>。2. 再看安全等级与来源。3. 最后看安装成本和权限边界。</p>
      <div class="meta-grid">
        <div class="meta-box"><dt>状态</dt><dd>verified 优先</dd></div>
        <div class="meta-box"><dt>安全</dt><dd>A / B 优先</dd></div>
        <div class="meta-box"><dt>来源</dt><dd>本地收录 + 公共上游更稳</dd></div>
        <div class="meta-box"><dt>安装</dt><dd>low 最适合快速试用</dd></div>
      </div>
    </aside>
  </div>
</section>
<main class="site-shell">
  <section class="section">
    <div class="section-head">
      <h2>先看这三类</h2>
      <p>把最常见的决策路径放到前面。</p>
    </div>
    <div class="quick-grid">{quick_html}</div>
  </section>
  <section class="section">
    <div class="section-head">
      <h2>按任务找</h2>
      <p>类别卡片会直接联动首页筛选器。</p>
    </div>
    <div class="category-grid">{category_html}</div>
  </section>
  <section class="section filters" id="skills">
    <div class="section-head">
      <h2>技能索引</h2>
      <p>优先显示高可信、低上手成本的技能。</p>
    </div>
    <div class="quick-pills">
      <button class="pill-button" data-quick-filter="recommended">推荐安装</button>
      <button class="pill-button" data-quick-filter="low-install">安装最轻</button>
      <button class="pill-button" data-quick-filter="safe">安全优先</button>
      <button class="pill-button" data-quick-filter="caution">需要谨慎</button>
      <button class="pill-button" data-quick-filter="reset">重置</button>
    </div>
    <div class="filter-grid">
      <label class="filter-field">搜索
        <input id="skill-search" type="search" placeholder="技能名、标签、场景、分类">
      </label>
      <label class="filter-field">状态
        <select id="status-filter">
          <option value="">全部</option>
          <option value="verified">verified</option>
          <option value="under_review">under_review</option>
          <option value="candidate">candidate</option>
        </select>
      </label>
      <label class="filter-field">安全
        <select id="security-filter">
          <option value="">全部</option>
          <option value="A">A</option>
          <option value="B">B</option>
          <option value="C">C</option>
          <option value="D">D</option>
        </select>
      </label>
      <label class="filter-field">分类
        <select id="category-filter">
          <option value="">全部</option>
          {category_options}
        </select>
      </label>
      <label class="filter-field">来源
        <select id="source-filter">
          <option value="">全部</option>
          <option value="local">local</option>
          <option value="external">external</option>
        </select>
      </label>
    </div>
    <div class="results-row">
      <p id="results-count" class="small">当前显示 {total} / {total} 个技能</p>
      <p class="small">点击卡片进入详情页。</p>
    </div>
    <div id="empty-state" class="empty-state">没有符合当前筛选条件的技能，建议先清空筛选器再看。</div>
    <div class="skill-grid">{cards_html}</div>
  </section>
  <section class="agent-panel reveal" id="agent">
    <h2>给 Agent 的稳定入口</h2>
    <p>静态站点和结构化 JSON 同步生成，便于后续接搜索、推荐或自动评估。</p>
    {agent_body}
  </section>
</main>
""",
    )


def build_trust_items(skill: dict[str, Any]) -> list[tuple[str, str]]:
    items = list(skill["trust"])
    existing = {key for key, _ in items}
    if not existing.intersection({"状态", "当前状态"}):
        items.append(("状态", f'{skill["status"]} / {skill["status_label"]}'))
    if not existing.intersection({"来源", "来源类型"}):
        items.append(("来源", skill["source_label"]))
    if not existing.intersection({"安全", "风险说明"}):
        items.append(("安全", f'{skill["security_grade"]} / {skill["security_note"]}'))
    if "维护者" not in existing:
        items.append(("维护者", skill["maintainer"]))
    if not existing.intersection({"最近验证日期", "最近验证"}):
        items.append(("最近验证日期", skill["last_verified_at"]))
    return items


def render_detail(skill: dict[str, Any], skills: list[dict[str, Any]]) -> str:
    related = related_skills(skill, skills)
    related_html = "".join(
        f'<a href="{item["detail_url"]}">{html.escape(item["name"])} · {html.escape(item["verdict_label"])}</a>'
        for item in related
    )
    if related_html:
        related_html = '<div class="related-links">' + related_html + '</div>'
    else:
        related_html = '<p class="muted">暂无可推荐的相邻技能。</p>'

    source_action = (
        f'<a class="btn-ghost" href="{html.escape(skill["source_url"], quote=True)}" target="_blank" rel="noreferrer">查看上游来源</a>'
        if skill["source_url"]
        else ""
    )

    review_panel = render_list(skill["review_notes"], css_class="review-list")
    comments_panel = render_comments(skill["comments"])

    return page_shell(
        f'{skill["name"]} - bxs-awesome-skills',
        skill["summary"],
        f"""
{render_topbar()}
<section class="detail-hero">
  <div class="site-shell detail-grid">
    <div class="hero-panel detail-copy reveal">
      <a class="back-link" href="/">返回首页</a>
      <p class="eyebrow">{html.escape(' / '.join(skill['categories'][:2]))}</p>
      <h1>{html.escape(skill['name'])}</h1>
      <p class="lede">{render_inline(skill['summary'])}</p>
      <div class="detail-actions">
        <a class="btn" href="{skill['data_url']}">打开 Skill JSON</a>
        {source_action}
      </div>
    </div>
    <aside class="trust-panel reveal">
      <span class="verdict verdict--{html.escape(skill['verdict'])}">{html.escape(skill['verdict_label'])}</span>
      <p class="small">{render_inline(skill['verdict_note'])}</p>
      <div class="meta-grid">
        <div class="meta-box"><dt>状态</dt><dd>{html.escape(skill['status_label'])}</dd></div>
        <div class="meta-box"><dt>安全</dt><dd>{html.escape(skill['security_grade'])}</dd></div>
        <div class="meta-box"><dt>安装</dt><dd>{html.escape(skill['install_label'])}</dd></div>
        <div class="meta-box"><dt>来源</dt><dd>{render_inline(skill['source_label'])}</dd></div>
        <div class="meta-box"><dt>最近验证</dt><dd>{html.escape(skill['last_verified_at'])}</dd></div>
        <div class="meta-box"><dt>已审核评论</dt><dd>{skill['comment_count']}</dd></div>
      </div>
    </aside>
  </div>
</section>
<main class="site-shell detail-panels">
  <div class="main-panels">
    <section class="section-panel reveal">
      <h2>快速判断</h2>
      {render_list(skill['quick_checks'])}
    </section>
    <section class="section-panel reveal">
      <h2>适合场景</h2>
      {render_list(skill['fit'])}
    </section>
    <section class="section-panel reveal">
      <h2>核心价值</h2>
      {render_list(skill['value'], ordered=True)}
    </section>
    <section class="section-panel reveal">
      <h2>最小上手</h2>
      {render_examples(skill['install_steps'])}
    </section>
    <section class="section-panel reveal">
      <h2>使用示例</h2>
      {render_examples(skill['usage_examples'])}
    </section>
    <section class="section-panel reveal">
      <h2>依赖与边界</h2>
      {render_key_values(skill['boundaries'])}
    </section>
    <section class="section-panel reveal">
      <h2>审核与反馈</h2>
      {review_panel}
      {comments_panel}
    </section>
  </div>
  <aside class="side-panels">
    <section class="section-panel reveal">
      <h2>信任与维护</h2>
      {render_key_values(build_trust_items(skill))}
    </section>
    <section class="section-panel reveal">
      <h2>兼容性</h2>
      {render_compatibility(skill['compatibility'])}
    </section>
    <section class="related-panel reveal">
      <h2>相关技能</h2>
      {related_html}
    </section>
    <section class="section-panel reveal">
      <h2>Agent 入口</h2>
      <ul class="agent-list">
        <li><a class="inline-link" href="{skill['data_url']}">{skill['data_url']}</a></li>
        <li>推荐字段：<code>verdict</code>、<code>security_grade</code>、<code>source_label</code>、<code>install_complexity</code></li>
        <li>可用标签：{render_inline('、'.join(skill['tags']) if skill['tags'] else '无')}</li>
      </ul>
    </section>
  </aside>
</main>
""",
    )


def render_not_found() -> str:
    return page_shell(
        "未找到页面 - bxs-awesome-skills",
        "返回首页继续浏览技能。",
        f"""
{render_topbar()}
<section class="hero">
  <div class="site-shell hero-grid">
    <div class="hero-panel reveal">
      <p class="eyebrow">404</p>
      <h1>这个页面不存在。</h1>
      <p class="lede">直接返回首页继续查找技能，或者用 JSON 索引交给 Agent 重新定位。</p>
      <div class="hero-actions">
        <a class="btn" href="/">返回首页</a>
        <a class="btn-ghost" href="/data/skills.json">查看 skills.json</a>
      </div>
    </div>
  </div>
</section>
""",
    )


def sort_skills(skills: list[dict[str, Any]]) -> list[dict[str, Any]]:
    verdict_rank = {"recommended": 0, "conditional": 1, "caution": 2}
    status_rank = {"verified": 0, "under_review": 1, "candidate": 2, "deprecated": 3, "archived": 4}
    security_rank = {"A": 0, "B": 1, "C": 2, "D": 3}
    return sorted(
        skills,
        key=lambda skill: (
            verdict_rank[skill["verdict"]],
            status_rank.get(skill["status"], 9),
            security_rank.get(skill["security_grade"], 9),
            skill["install_complexity"] != "low",
            -skill["quality_score"],
            skill["name"],
        ),
    )


def ensure_dist() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "assets").mkdir(parents=True)
    (DIST / "skills").mkdir(parents=True)
    (DIST / "data" / "skills").mkdir(parents=True)
    for asset in ASSETS_DIR.iterdir():
        shutil.copy2(asset, DIST / "assets" / asset.name)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    categories_payload = load_yaml(ROOT / "catalog" / "categories.yaml")
    skills_payload = load_yaml(ROOT / "catalog" / "skills.yaml")
    categories = sorted(categories_payload["categories"], key=lambda item: item.get("order", 999))
    comments_map = load_comments()
    skills = [build_skill_payload(skill, comments_map) for skill in skills_payload["skills"]]
    skills = sort_skills(skills)

    ensure_dist()

    write_text(DIST / "index.html", render_home(skills, categories, str(skills_payload.get("updated_at", ""))))
    write_text(DIST / "404.html", render_not_found())
    write_json(DIST / "data" / "skills.json", skills)
    write_json(DIST / "data" / "categories.json", categories)

    for skill in skills:
        write_text(DIST / "skills" / skill["slug"] / "index.html", render_detail(skill, skills))
        write_json(DIST / "data" / "skills" / f'{skill["slug"]}.json', skill)

    print(f"Built site in {DIST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
