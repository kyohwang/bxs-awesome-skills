---
slug: github-daily-report
name:
  zh: GitHub 每日三段式日报
  en: GitHub Daily Report
summary:
  zh: 生成 GitHub 总榜/增长榜/新锐榜三段式中文日报。
  en: Generate Chinese daily GitHub reports with three ranking sections.
source:
  type: local
  url: null
  local_path: skills/github-daily-report
category:
  - 我想写代码/修 Bug
  - 我想做研究与信息整理
tags:
  - github
  - report
  - analysis
status: under_review
quality_score: 60
security_grade: D
install_complexity: medium
last_verified_at: null
---

# GitHub 每日三段式日报

## 1. 适用场景

- 每日追踪 GitHub 热门与增长项目
- 需要固定三段式播报模板（总榜/增长榜/新锐榜）
- 技术情报晨报/晚报自动化

## 2. 核心功能

1. 抓取候选仓库并写入本地快照。
2. 计算 24h 增长并输出三段式日报。
3. 输出可直接转发的中文内容格式。

## 3. 最简安装（3 步）

```bash
mkdir -p .claude/skills
cp -r skills/github-daily-report .claude/skills/
python3 /data/github_daily_report.py report
```

## 4. 使用方式

采样：

```bash
python3 /data/github_daily_report.py collect
```

生成日报：

```bash
python3 /data/github_daily_report.py report
```

## 5. 依赖与权限

- 运行依赖：`python3`、GitHub API、SQLite 数据文件
- 环境变量：`GITHUB_TOKEN`
- 网络访问：需要（GitHub API）
- 敏感操作：涉及外部数据采集，不涉及破坏性写操作

## 6. 安全信息

- 安全等级：`D`
- 依据摘要：尚未完成最新一轮安全审计与验证记录补齐

## 7. 维护状态

- 当前状态：`under_review`
- 维护者：`OpenClaw Agent`
- 最近验证日期：`null`（待补）

## 8. 评论摘要（默认 3 条）

- 暂无已审核评论，详见 `comments/github-daily-report.yaml`

## 9. 审核记录

- `2026-03-02` 标记为待复审（需补安全审计）
