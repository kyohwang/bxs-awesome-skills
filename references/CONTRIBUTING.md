# Contributing / 贡献指南

## 中文

### 目标

仓库以“高质量、可审计、可复用”为优先，不以数量为目标。

### 收录硬规则

1. 新技能必须先进入 `proposals/`。
2. 必须通过 `skill-security-audit`（无 BLOCK）。
3. 必须由 Owner 明确批准。
4. 才能进入 `skills/`。

### 必需文件

每个正式技能目录至少包含：

- `SKILL.md`
- `skill.json`
- `README.md`（技能独立信息页，中文必填，英文可选）

### 索引与分类（v0.3）

提交新技能时，必须同步更新：

- `skills/index.json`（兼容层）
- `catalog/skills.yaml`（发现与治理主索引）

分类必须从 `catalog/categories.yaml` 选择，不可自造类目。

### 评论与审核

1. 用户评论入口：GitHub Discussions。
2. 展示规则：只展示已审核摘要。
3. 数据落地：`comments/<slug>.yaml`。
4. 技能页默认显示最近 3 条已审核评论。

### 自动化与合并规则

允许自动合并的仅限低风险变更（白名单）：

- 链接修复、拼写修复、非关键元数据补全
- 审核通过评论摘要同步

必须人工审核的高风险变更：

- 新增/下架技能
- 安全等级跨级变化
- 安装命令、权限边界、审核规则变更

### 命名规范

- 目录与 slug 使用小写连字符（kebab-case）
- 技能目录名与 `skill.json` 中 `name` 建议保持一致

## English

### Goal

Quality, auditability, and reuse first. Quantity is not the objective.

### Hard admission rules

1. New skills start in `proposals/`.
2. Must pass `skill-security-audit` (no BLOCK findings).
3. Must receive explicit owner approval.
4. Then it can be promoted into `skills/`.

### Required files

Each admitted skill directory should include:

- `SKILL.md`
- `skill.json`
- `README.md` (Chinese-first profile, optional English supplement)

### Indexing (v0.3)

Contributors must update both:

- `skills/index.json` (compatibility layer)
- `catalog/skills.yaml` (primary discovery/governance index)

### Reviews and comments

- Comment intake via GitHub Discussions.
- Only approved comment summaries are shown.
- Structured outputs live in `comments/<slug>.yaml`.

### Merge policy

- Low-risk changes may be auto-merged.
- High-risk changes require human review.
