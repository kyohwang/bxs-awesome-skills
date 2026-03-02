# bxs-awesome-skills

高质量 Skills 索引与评估库，面向人类用户与 AI Agent。  
目标是让你在最短时间内判断：**这个 skill 值不值得安装**。

> Language policy: 中文为主，英文可选补充。

## 快速开始

1. 按“你要完成的任务”进入分类目录。
2. 先看标签：`状态`、`安全等级`、`安装复杂度`、`维护活跃度`。
3. 打开 skill 详情页，确认最简安装与评论摘要后再安装。

## 快速决策筛选

- `推荐安装`：`status=verified` 且 `security_grade=A/B` 且 `quality_score>=75`
- `安装最简单`：`install_complexity=low`
- `近期活跃`：`last_verified_at<=30 天` 且上游最近提交 `<=90 天`
- `低风险优先`：`security_grade=A/B`

## 分类目录（用户目标导向）

### 我想写代码/修 Bug

- [GitHub 每日三段式日报](skills/github-daily-report/README.md) - 生成总榜/增长榜/新锐榜日报 | `[状态:under_review] [安全:D] [安装:medium] [来源:local]`
- [MCPorter CLI 操作技能](skills/mcporter-cli-opskill/README.md) - MCP 工具可审计调用与检查 | `[状态:verified] [安全:A] [安装:medium] [来源:local]`

### 我想自动执行任务

- [ClawHub CLI 技能](skills/clawhub/README.md) - 检索、安装、更新、发布 skills | `[状态:verified] [安全:A] [安装:medium] [来源:local]`
- [MCPorter CLI 操作技能](skills/mcporter-cli-opskill/README.md) - MCP 工具可审计调用与检查 | `[状态:verified] [安全:A] [安装:medium] [来源:local]`
- [小红书 MCP 发布助手](skills/xiaohongshu-mcp-publisher/README.md) - 先审后发的小红书发布流程 | `[状态:verified] [安全:A] [安装:medium] [来源:local]`

### 我想做研究与信息整理

- [GitHub 每日三段式日报](skills/github-daily-report/README.md) - 技术情报日报生成 | `[状态:under_review] [安全:D] [安装:medium] [来源:local]`

### 我想处理数据

- 暂无条目（待收录）

### 我想做内容与设计

- [小红书 MCP 发布助手](skills/xiaohongshu-mcp-publisher/README.md) - 图文发布编排与诊断 | `[状态:verified] [安全:A] [安装:medium] [来源:local]`

### 我想做协作与办公

- [ClawHub CLI 技能](skills/clawhub/README.md) - 团队级技能分发与升级 | `[状态:verified] [安全:A] [安装:medium] [来源:local]`

### 我关心安全与系统管理

- [Skill 安全审计](skills/skill-security-audit/README.md) - 提案技能安全准入与复审 | `[状态:verified] [安全:A] [安装:low] [来源:local]`

## 收录流程（硬门槛）

统一采用：

`proposal -> security-audit -> owner approve -> skills/`

详细规范：

- `references/CONTRIBUTING.md`
- `references/PROPOSAL_TEMPLATE.md`
- `references/SKILL_MANIFEST.schema.json`

## 元数据与兼容说明

当前仓库同时维护两套索引：

- 旧索引：`skills/index.json`（保持兼容）
- 新索引：`catalog/skills.yaml`（面向发现、评估与治理）

分类配置：`catalog/categories.yaml`  
技能页模板：`templates/skill-profile.template.md`  
产品需求文档：`prd.md`

## 目录结构

```text
skills/           # 已审核通过或待复审技能（含 SKILL.md 与 skill.json）
skills/_template/ # 技能模板（历史）
proposals/        # 待审核候选技能说明
references/       # 规范与参考文档
catalog/          # 新版分类与技能索引
templates/        # 新版技能详情页模板
comments/         # 已审核评论摘要
```
