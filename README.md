# bxs-awesome-skills

先判断一个 skill 值不值得装，再决定怎么装。

## 怎么选

1. 先看 `状态`：优先 `verified`。
2. 再看 `安全` 和 `来源`：优先 `A/B`，且有公开上游。
3. 最后看 `安装成本` 和 `权限边界`：先试 `low`，再决定是否接入更重的 skill。

## 快速索引

| Skill | 解决什么问题 | 状态 | 安全 | 安装 | 来源 |
| --- | --- | --- | --- | --- | --- |
| [ClawHub CLI 技能](skills/clawhub/README.md) | 搜索、安装、更新、发布 skills | `verified` | `A` | `medium` | 本地收录 / `clawhub.ai` |
| [Skill 安全审计](skills/skill-security-audit/README.md) | 对候选 skill 做安全准入审计 | `verified` | `A` | `low` | 本地收录 |
| [MCPorter CLI 操作技能](skills/mcporter-cli-opskill/README.md) | 以可审计方式调用 MCP 工具 | `verified` | `A` | `medium` | 本地收录 / OpenClaw 上游 |
| [小红书 MCP 发布助手](skills/xiaohongshu-mcp-publisher/README.md) | 先审后发的小红书发布流程 | `verified` | `A` | `medium` | 本地收录 / GitHub 上游 |
| [GitHub 每日三段式日报](skills/github-daily-report/README.md) | 生成 GitHub 中文日报 | `under_review` | `D` | `medium` | 本地收录 |

## 先看这几类

- `推荐安装`：`clawhub`、`skill-security-audit`、`mcporter-cli-opskill`
- `安装最轻`：`skill-security-audit`
- `需要谨慎`：`github-daily-report`

## 给 Agent 的稳定入口

- 源数据：[`catalog/skills.yaml`](catalog/skills.yaml)、[`catalog/categories.yaml`](catalog/categories.yaml)
- 兼容层：[`skills/index.json`](skills/index.json)
- Cloudflare Pages 构建后：`/data/skills.json`、`/data/categories.json`、`/data/skills/<slug>.json`

## Cloudflare Pages

- 构建命令：`python3 scripts/build_site.py`
- 输出目录：`dist`
- 站点目标：人类可快速浏览，Agent 可直接抓取稳定 JSON

## 收录规则

- 新技能必须先进入 `proposals/`
- 必须通过 `skill-security-audit`，不能有 `BLOCK`
- 必须由 Owner 明确批准后才能进入 `skills/`
- 收录时同步更新 `catalog/skills.yaml`、`skills/index.json` 和 `comments/<slug>.yaml`
