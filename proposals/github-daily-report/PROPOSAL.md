# Proposal: github-daily-report

## 来源（必填）
- 类型：内部原创（可追溯）
- 代码来源：`/data/github_daily_report.py`
- 依赖来源：GitHub REST API v3（search/repositories, repos/{owner}/{repo}）

## 目标
产出 GitHub 三段式日报（总榜/增长榜/新锐榜），用于每日早报。

## 适用场景
- 需要每天自动拉取 GitHub 热门仓库变化
- 需要稳定输出中文三段式榜单

## 最小可运行示例
```bash
python3 /data/github_daily_report.py report
```

## 边界行为
- 无 `GITHUB_TOKEN`：应失败并提示 `Missing GITHUB_TOKEN`
- 非法模式参数：应失败并提示 `Usage: github_daily_report.py [collect|report]`
