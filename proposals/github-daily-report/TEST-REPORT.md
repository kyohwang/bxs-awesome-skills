# github-daily-report Test Report

## Minimal runnable example

Command:
```bash
python3 /data/github_daily_report.py report
```

Result: PASS (2026-02-24 UTC)
- Exit code: 0
- Output contains required three sections:
  - 🏆 总榜 Top10（按 Star 总量）
  - 📈 增长榜 Top10（按 24h 增长量）
  - 🚀 新锐榜 Top10（★>5000，按 24h 增长幅度）

## Boundary checks

- Missing `GITHUB_TOKEN`: expected failure with `Missing GITHUB_TOKEN` (covered by script guard)
- Invalid mode: expected failure with `Usage: github_daily_report.py [collect|report]` (covered by script guard)
