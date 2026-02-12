# Whitelist Policy (Draft)

- Owner approval required for each whitelist entry.
- Mandatory fields: `rule_id`, `path_scope`, `reason`, `approved_by`, `expired_at`.
- Default TTL: 30 days.
- Expired entries are ignored automatically.
- Every whitelist hit must still be logged in report output.
