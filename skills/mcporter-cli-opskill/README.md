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

> 如果你要让 Agent 以可审计方式调用 MCP 工具，而不是盲调工具，这是更稳的做法。

## 快速判断

- 值不值得装：推荐安装。尤其适合需要“先只读、后确认写入”的 MCP 工作流。
- 最适合：检查 server 配置、列出工具能力、执行结构化工具调用。
- 来源：本地收录，公开上游为 OpenClaw 官方 `mcporter` skill。
- 安全：`A`，默认只读优先，写操作需显式确认参数和目标。
- 上手成本：`medium`，需要已安装 `mcporter` CLI。

## 适合场景

- 需要检查 MCP server 配置和工具 schema
- 需要执行可审计的 MCP 工具调用
- 需要在自动化流程中明确写操作边界

## 核心价值

1. 可以快速列出 server 和工具能力，先看清楚再调用。
2. `mcporter call` 提供结构化调用方式，便于记录参数和结果。
3. 对写操作保持谨慎边界，适合安全要求更高的自动化流程。

## 最小上手

```bash
mkdir -p .claude/skills
cp -r skills/mcporter-cli-opskill .claude/skills/
mcporter --help
```

安装后验证：

```bash
mcporter list
```

## 使用示例

只读检查：

```bash
mcporter list
mcporter list <server> --schema
```

工具调用：

```bash
mcporter call <server.tool> key=value
```

## 依赖与边界

- 运行依赖：`mcporter` CLI
- 环境变量：按目标 MCP server 决定
- 网络访问：取决于目标 MCP server
- 文件系统权限：通常不需要额外本地写权限
- 敏感操作：写操作前必须确认参数、目标和预期副作用

## 信任与维护

- 当前状态：`verified`
- 来源类型：`local`，上游为 OpenClaw 官方 `mcporter` skill
- 维护者：`OpenClaw Agent`
- 最近验证日期：`2026-02-24`
- 兼容性：`Claude Code(compatible)`、`OpenAI Agents(compatible)`、`Gemini CLI(compatible)`、`OpenClaw(native)`

## 审核与反馈

- 审核结论：推荐用于需要审计链路的 MCP CLI 调用场景。
- 已审核评论：暂无，见 `comments/mcporter-cli-opskill.yaml`
- 审核记录：`2026-02-24` 复审通过
