---
name: mcporter-cli-opskill
description: Use mcporter to inspect MCP server configs and run direct MCP tool calls with explicit, auditable command patterns.
---

# mcporter-cli-opskill

来源

- OpenClaw 官方 `mcporter` skill: `/usr/lib/node_modules/openclaw/skills/mcporter/SKILL.md`
- mcporter CLI 帮助输出：`mcporter --help`

最小可用命令

- `mcporter --help`
- `mcporter list`
- `mcporter list <server> --schema`

常用操作

- 调用工具：`mcporter call <server.tool> key=value`
- OAuth 认证：`mcporter auth <server | url> [--reset]`
- 配置管理：`mcporter config list|get|add|remove|import|login|logout`
- 代码生成：`mcporter generate-cli --server <name>`

边界与安全约束

- 默认只做只读检查：优先 `list`、`--schema`、`--help`。
- 任何写操作（例如 create/update/delete）必须先显式确认目标与参数。
- 不在命令里内联密钥；敏感值通过环境变量或安全存储注入。
- 不对未知第三方 URL 执行 `mcporter call`，除非先完成安全审计。
