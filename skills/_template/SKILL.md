---
name: your-skill-name
description: Describe exactly what this skill does and when it should be used.
---

# Skill Title

## Objective

State the exact outcome this skill should produce.

## Inputs

List required and optional inputs.

## Workflow

1. Step one
2. Step two
3. Step three

## Output

Define the output format and quality bar.

## Guardrails

- Keep operations safe and reversible when possible.
- Ask before external side effects.

## Required companion file

Create `skill.json` next to `SKILL.md` and validate it against:
`references/SKILL_MANIFEST.schema.json`

`skill.json` must include:
- install commands
- compatibility labels (claude-code/openai-agents/gemini-cli/openclaw)
- quality metrics (security_score, real_world_validated, maintainer, last_verified_at)
