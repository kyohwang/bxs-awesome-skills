# mcporter-cli-opskill Test Report

## Install test
Command:
```bash
mkdir -p /tmp/skill-install-test/.claude/skills
cp -r proposals/mcporter-cli-opskill/candidate /tmp/skill-install-test/.claude/skills/mcporter-cli-opskill
```
Result: PASS
- Installed files:
  - `SKILL.md`
  - `skill.json`

## Minimal runnable examples
Command:
```bash
mcporter --help | head -n 8
mcporter list
```
Result: PASS
- `mcporter --help` returns usage docs successfully.
- `mcporter list` returns `No MCP servers configured.` in empty environment (expected).

## Boundary checks
Command:
```bash
mcporter call
mcporter list __not_exist__ --schema
```
Result: PASS
- Missing required selector returns explicit error: `Missing server name. Provide it via <server>.<tool> or --server.`
- Unknown server returns explicit error: `Unknown MCP server '__not_exist__'.`
