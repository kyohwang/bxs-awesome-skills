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

> 功能定位很清楚，但当前仍在复审中；如果你重视可信度，应先看审计和依赖补齐情况。

## 快速判断

- 值不值得装：暂缓安装。功能明确，但当前状态是 `under_review`，安全等级为 `D`。
- 最适合：技术情报日报自动化、GitHub 热门和增长项目追踪。
- 来源：本地收录，当前没有公开上游地址可复核。
- 安全：`D`，最新一轮安全审计和验证记录尚未补齐。
- 上手成本：`medium`，需要 `python3`、GitHub API 和本地数据文件。

## 适合场景

- 每日追踪 GitHub 热门与增长项目
- 需要固定三段式播报模板（总榜 / 增长榜 / 新锐榜）
- 技术情报晨报或晚报自动化

## 核心价值

1. 自动采样候选仓库并输出统一格式的中文日报，节省整理时间。
2. 把总榜、增长榜和新锐榜拆开，适合内容分发和运营复用。
3. 结果更像成品内容，而不是原始数据表。

## 最小上手

```bash
mkdir -p .claude/skills
cp -r skills/github-daily-report .claude/skills/
python3 /data/github_daily_report.py report
```

安装后验证：

```bash
python3 /data/github_daily_report.py collect
```

## 使用示例

采样：

```bash
python3 /data/github_daily_report.py collect
```

生成日报：

```bash
python3 /data/github_daily_report.py report
```

## 依赖与边界

- 运行依赖：`python3`、GitHub API、SQLite 数据文件
- 环境变量：`GITHUB_TOKEN`
- 网络访问：需要，调用 GitHub API
- 文件系统权限：会读写本地数据快照
- 敏感操作：不涉及破坏性写操作，但会拉取外部数据并生成内容

## 信任与维护

- 当前状态：`under_review`
- 来源类型：`local`
- 风险说明：公开上游、最新安全审计和验证记录均待补齐
- 维护者：`OpenClaw Agent`
- 最近验证日期：未记录
- 兼容性：`Claude Code(compatible)`、`OpenAI Agents(compatible)`、`Gemini CLI(compatible)`、`OpenClaw(native)`

## 审核与反馈

- 审核结论：当前不建议直接用于生产流程，先补安全审计再评估。
- 已审核评论：暂无，见 `comments/github-daily-report.yaml`
- 审核记录：`2026-03-02` 标记为待复审，需补安全审计
