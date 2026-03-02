# bxs-awesome-skills

高质量 Skills 索引与评估库，面向人类用户与 AI Agent。  
目标是让你在最短时间内判断：**这个 skill 值不值得安装**。

## 使用方法

1. 按“你要完成的任务”进入分类目录。
2. 先看标签：`状态`、`安全等级`、`安装复杂度`、`维护活跃度`。
3. 打开 skill 详情页，确认最简安装与评论摘要后再安装。

## 快速筛选

- `推荐安装`：`status=verified` 且 `security_grade=A/B` 且 `quality_score>=75`
- `安装最简单`：`install_complexity=low`
- `近期活跃`：`last_verified_at<=30 天` 且上游最近提交 `<=90 天`
- `低风险优先`：`security_grade=A/B`

## 标签说明

- `状态`：`candidate / under_review / verified / deprecated / archived`
- `安全`：`A / B / C / D`（前台仅展示等级）
- `安装`：`low / medium / high`
- `来源`：`local / external`

## 技能目录

### 代码与调试

- [GitHub 每日三段式日报](skills/github-daily-report/README.md) - 生成总榜/增长榜/新锐榜日报 | `[状态:under_review] [安全:D] [安装:medium] [来源:local]`
- [MCPorter CLI 操作技能](skills/mcporter-cli-opskill/README.md) - MCP 工具可审计调用与检查 | `[状态:verified] [安全:A] [安装:medium] [来源:local]`

### 自动化执行

- [ClawHub CLI 技能](skills/clawhub/README.md) - 检索、安装、更新、发布 skills | `[状态:verified] [安全:A] [安装:medium] [来源:local]`
- [MCPorter CLI 操作技能](skills/mcporter-cli-opskill/README.md) - MCP 工具可审计调用与检查 | `[状态:verified] [安全:A] [安装:medium] [来源:local]`
- [小红书 MCP 发布助手](skills/xiaohongshu-mcp-publisher/README.md) - 先审后发的小红书发布流程 | `[状态:verified] [安全:A] [安装:medium] [来源:local]`

### 研究与信息整理

- [GitHub 每日三段式日报](skills/github-daily-report/README.md) - 技术情报日报生成 | `[状态:under_review] [安全:D] [安装:medium] [来源:local]`

### 数据处理

- 暂无条目（待收录）

### 内容与发布

- [小红书 MCP 发布助手](skills/xiaohongshu-mcp-publisher/README.md) - 图文发布编排与诊断 | `[状态:verified] [安全:A] [安装:medium] [来源:local]`

### 协作与办公

- [ClawHub CLI 技能](skills/clawhub/README.md) - 团队级技能分发与升级 | `[状态:verified] [安全:A] [安装:medium] [来源:local]`

### 安全与系统

- [Skill 安全审计](skills/skill-security-audit/README.md) - 提案技能安全准入与复审 | `[状态:verified] [安全:A] [安装:low] [来源:local]`

## 安装

- 项目级安装：`cp -r skills/<slug> .claude/skills/`
- 用户级安装：`cp -r skills/<slug> ~/.claude/skills/`
- 具体依赖与最简步骤：见各技能页面

## 贡献

- 新技能提案与审核流程：`references/CONTRIBUTING.md`
