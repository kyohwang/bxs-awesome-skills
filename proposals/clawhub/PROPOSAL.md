# Skill Proposal: clawhub

## 1) Basic Info
- Skill name: clawhub
- Category: Automation
- Owner: OpenClaw Agent
- Source: OpenClaw official `clawhub` skill (`/usr/lib/node_modules/openclaw/skills/clawhub/SKILL.md`), upstream https://clawhub.com

## 2) What problem it solves
- One-sentence positioning: Standardize ClawHub CLI usage for searching, installing, updating, and publishing agent skills.
- Target users/scenarios: Skill maintainers and operators who need repeatable skill distribution workflows.

## 3) Inputs / Outputs
- Inputs: skill keyword/slug/version and local skill directory path.
- Outputs: searchable/installable skill operations and publish commands.
- Failure behavior: return CLI/network/auth error and require explicit remediation (login, retry, or version pin).

## 4) Install & Usage
- Install command/path: `cp -r skills/clawhub .claude/skills/`
- Invocation examples:
  - `clawhub search "postgres backups"`
  - `clawhub install my-skill --version 1.2.3`
  - `clawhub update --all --no-input --force`

## 5) Security & Risk Boundary
- Required permissions: outbound HTTPS to ClawHub registry and optional npm install capability.
- External side effects: may download/install skill files; publish path can push metadata to ClawHub.
- Data handling policy: do not publish secrets; require explicit user confirmation before publish actions.

## 6) Compatibility Labels
- claude-code: compatible
- openai-agents: compatible
- gemini-cli: compatible
- openclaw: native

## 7) Quality Metrics (initial)
- security_score: 0
- real_world_validated: true
- maintainer: OpenClaw Agent
- last_verified_at: 2026-02-24T22:30:00Z

## 8) Evidence
- security report path: `proposals/clawhub/SECURITY-REPORT.generated.json`
- demo/test proof: `proposals/clawhub/TEST-REPORT.md`
