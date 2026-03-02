---
slug: mcporter-cli-opskill
name:
  zh: MCPorter CLI 操作技能
  en: MCPorter CLI Opskill
summary:
  zh: 使用 mcporter 执行 MCP 工具检查与可审计调用。
  en: Auditable MCP tool operations and inspections via mcporter CLI.
source:
  type: local
  url: https://github.com/openclaw/openclaw/tree/main/skills/mcporter
  local_path: skills/mcporter-cli-opskill
category:
  - 我想自动执行任务
  - 我想写代码/修 Bug
tags:
  - mcp
  - cli
  - automation
status: verified
quality_score: 84
security_grade: A
install_complexity: medium
last_verified_at: 2026-02-24T19:31:31Z
---

# MCPorter CLI 操作技能

## 1. 适用场景

- 需要检查 MCP server 配置和工具 schema
- 需要执行可审计的 MCP 工具调用
- 需要在自动化流程中明确写操作边界

## 2. 核心功能

1. 快速列出 server 与工具能力。
2. 通过 `mcporter call` 进行结构化工具调用。
3. 强制遵循“先只读、后确认写入”的安全边界。

## 3. 最简安装（3 步）

```bash
mkdir -p .claude/skills
cp -r skills/mcporter-cli-opskill .claude/skills/
mcporter --help
```

## 4. 使用方式

只读检查：

```bash
mcporter list
mcporter list <server> --schema
```

工具调用：

```bash
mcporter call <server.tool> key=value
```

## 5. 依赖与权限

- 运行依赖：`mcporter` CLI
- 网络访问：按目标 MCP server 决定
- 敏感操作：写操作前必须确认参数与目标

## 6. 安全信息

- 安全等级：`A`
- 依据摘要：默认只读优先，写操作需显式确认

## 7. 维护状态

- 当前状态：`verified`
- 上游来源：OpenClaw 官方 mcporter skill
- 维护者：`OpenClaw Agent`
- 最近验证日期：`2026-02-24T19:31:31Z`

## 8. 评论摘要（默认 3 条）

- 暂无已审核评论，详见 `comments/mcporter-cli-opskill.yaml`

## 9. 审核记录

- `2026-02-24` 复审通过
