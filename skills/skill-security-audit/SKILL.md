---
name: skill-security-audit
description: Audit candidate Agent Skills for malicious or unsafe patterns before admission. Use when reviewing skills in proposals/, before promoting to skills/, or when re-validating existing skills for security regressions.
---

# skill-security-audit

## Objective

Perform a strict security audit for a target skill directory and output a deterministic verdict:
- `PASS`
- `REVIEW`
- `BLOCK`

No whitelist bypass by default.

## Inputs

- Target directory (required)
- Rules file (optional, default: `references/security-rules.json`)
- Output path (optional)

## Workflow

1. Run local static audit:

```bash
python3 scripts/skill_security_audit.py <target_dir> --out SECURITY-REPORT.generated.json
```

2. (Optional but recommended) Run MCP engine scan:

```bash
bash scripts/run_mcp_scan.sh <target_dir> mcp-scan-report.json
```

3. Determine admission decision:
- Any `BLOCK` finding => reject admission
- Score >= 85 and no `BLOCK` => pass
- Otherwise => manual review

## Output Contract

Must include:
- verdict
- score
- high_risk_count
- review_count
- findings[] with evidence schema (`references/evidence-schema.json`)

## Admission Policy

- New skills must be audited before entering `skills/`
- This audit is strict mode by default (no bypass)
- Keep evidence traceable (path + line + snippet + fix hint)

## References

- `references/security-rules.json`
- `references/evidence-schema.json`
- `references/whitelist-policy.md`
