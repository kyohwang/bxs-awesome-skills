---
name: github-daily-report
description: 生成 GitHub 三段式日报（总榜/增长榜/新锐榜）。用于每日技术情报播报：抓取候选仓库、写入本地快照、计算 24h 增长并输出可直接发送的中文日报。
---

# github-daily-report

## 来源
- 内部脚本：`/data/github_daily_report.py`
- API：GitHub REST API

## 安装
```bash
mkdir -p .claude/skills
cp -r skills/github-daily-report .claude/skills/
```

## 运行前提
- 已设置 `GITHUB_TOKEN`（环境变量或 `/data/.secrets/github.env`）
- 本地 SQLite：`/data/github_reports.db`

## 标准用法
1. 采样：
```bash
python3 /data/github_daily_report.py collect
```
2. 生成日报（自动补采样）：
```bash
python3 /data/github_daily_report.py report
```

## 输出约定
必须输出三段：
- 🏆 总榜 Top10（按 Star 总量）
- 📈 增长榜 Top10（按 24h 增长量）
- 🚀 新锐榜 Top10（★>5000，按 24h 增长幅度）

## 审核门槛
- 输出必须包含三段标题
- 每段默认 10 条
- 同一 repo 不应在“总榜”90 天内反复占位（脚本内置去重）
