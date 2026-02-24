# Skill Proposal: mcporter-cli-opskill

## 1) Basic Info
- Skill name: mcporter-cli-opskill
- Category: Automation
- Owner: OpenClaw Agent
- Source:
  - OpenClaw official `mcporter` skill: `/usr/lib/node_modules/openclaw/skills/mcporter/SKILL.md`
  - Upstream reference: `https://github.com/openclaw/openclaw/tree/main/skills/mcporter`

## 2) What problem it solves
- One-sentence positioning: provide auditable CLI playbooks for MCP server discovery/config/calls using `mcporter`.
- Target users/scenarios: operators who need standardized MCP diagnostics and safe call patterns.

## 3) Inputs / Outputs
- Inputs: server name, tool selector (`server.tool`), and key=value args.
- Outputs: server list/schema output, tool call response, or explicit error hints.
- Failure behavior: return deterministic CLI errors for missing selector and unknown server.

## 4) Install & Usage
- Install command/path: `cp -r skills/mcporter-cli-opskill .claude/skills/`
- Minimal examples:
  - `mcporter --help`
  - `mcporter list`
  - `mcporter list <server> --schema`

## 5) Security & Risk Boundary
- Required permissions: local CLI execution and optional network access only when user explicitly runs remote MCP calls.
- External side effects: potential remote MCP tool calls; default guidance is read-only checks first.
- Data handling policy: never inline secrets in command args; inject via env/secure storage.

## 6) Compatibility Labels
- claude-code: compatible
- openai-agents: compatible
- gemini-cli: compatible
- openclaw: native

## 7) Quality Metrics (verified)
- security_score: 92
- real_world_validated: true
- maintainer: OpenClaw Agent
- last_verified_at: 2026-02-24T19:31:31Z

## 8) Evidence
- security report path: `proposals/mcporter-cli-opskill/SECURITY-REPORT.generated.json`
- demo/test proof: `proposals/mcporter-cli-opskill/TEST-REPORT.md`
