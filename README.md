# bxs-awesome-skills

[中文](#中文) | [English](#english)

---

## 中文

这是一个给 Agent 用的 **Skills 兵器谱**。

灵感来自《兵器谱》：
江湖不缺兵器，缺的是靠谱兵器。

这个仓库不追求“收得多”，而追求“收得准”：
- 分门别类
- 安全靠谱
- 真实有效

### 仓库定位

- 它是一个 Skills 排行榜 + 搜集仓库
- 它记录“什么技能好用、为什么好用、在什么场景最好用”
- 它不是广告位，不收空壳技能

### 核心目标

- 沉淀可复用的 Agent Skills
- 提供统一结构、规范和审核流程
- 以内容共享为主，只维护代码与文档

### 收录规则（当前生效）

1. 技能由维护者（Agent）提出候选
2. 每个技能必须经过 Owner 明确审核同意
3. 审核通过后才能进入 `skills/` 正式目录
4. 默认 `main` 直推

### 评分与排行（兵器谱）

后续将按以下维度维护排行榜：

- **有效性**：是否稳定解决真实问题
- **安全性**：是否遵循最小权限、可审计、可回滚
- **可复用性**：是否能跨项目重复使用
- **可维护性**：结构是否清晰，依赖是否可控
- **实战反馈**：是否有真实使用记录与结果

> 原则：宁缺毋滥。没有实战价值的技能，不进榜。

### 分类体系（持续扩展）

- 内容生产（Content）
- 发布分发（Publishing）
- 自动化流程（Automation）
- 开发协作（Dev & GitHub）
- 数据与研究（Data & Research）
- 运维与安全（Ops & Security）

### 目录结构

```text
skills/           # 已审核通过的正式技能
skills/_template/ # 技能模板
proposals/        # 待审核候选技能说明
references/       # 规范与参考文档
scripts/          # 辅助脚本
```

### 技能最小标准

- 必须有 `SKILL.md`
- 必须包含 frontmatter:
  - `name`
  - `description`
- `description` 必须写清楚“何时触发”
- 需要说明边界与风险（尤其是外部动作）

### 当前状态

- 已初始化技能市场骨架
- 已启用候选审核流程（逐个确认）
- 将逐步补齐“兵器谱排行榜”与分类索引

---

## English

This is a **Skills Armory** for agents.

Inspired by classic weapon rankings: the world has many tools, but very few truly reliable ones.

This repo optimizes for quality over quantity:
- Clear taxonomy
- Safety and reliability
- Real-world effectiveness

### Positioning

- A skills leaderboard + curated collection
- It records what works, why it works, and where it works best
- Not a dumping ground for low-quality skills

### Core Goals

- Curate reusable Agent Skills
- Provide consistent structure, standards, and review workflow
- Focus on shared content (code + docs only)

### Admission Policy (active)

1. Candidate skills are proposed by the maintainer agent.
2. Every skill requires explicit owner approval.
3. Only approved skills can be moved into `skills/`.
4. Default workflow: direct push to `main`.

### Ranking Criteria (Armory Board)

Leaderboard maintenance will use these dimensions:

- **Effectiveness**: solves real tasks reliably
- **Safety**: least privilege, auditable, reversible
- **Reusability**: works across projects
- **Maintainability**: clear structure and manageable dependencies
- **Field feedback**: backed by real usage outcomes

> Principle: quality first. No proven value, no ranking.

### Taxonomy (expanding)

- Content
- Publishing
- Automation
- Dev & GitHub
- Data & Research
- Ops & Security

### Repository Layout

```text
skills/           # approved production skills
skills/_template/ # skill template
proposals/        # pending skill proposals for review
references/       # references and conventions
scripts/          # helper scripts
```

### Minimum Skill Requirements

- Must include `SKILL.md`
- Must include frontmatter:
  - `name`
  - `description`
- `description` must clearly state trigger contexts
- Must document boundaries and risks (especially external side effects)

### Current Status

- Marketplace skeleton initialized
- Candidate review workflow active
- Armory leaderboard and category index to be expanded incrementally
