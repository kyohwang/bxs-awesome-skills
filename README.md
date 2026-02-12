# bxs-awesome-skills

[中文](#中文) | [English](#english)

---

## 中文

面向 Agent 的技能市场仓库。

### 仓库目标

- 沉淀可复用的 Agent Skills
- 提供统一的结构、规范和审核流程
- 以“内容共享”为主，只维护代码与文档

### 收录规则（当前生效）

1. 技能由维护者（Agent）提出候选
2. 每个技能必须经过 Owner 明确审核同意
3. 审核通过后才能进入 `skills/` 正式目录
4. 默认 `main` 直推

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

### 当前状态

- 已初始化技能市场骨架
- 待提交候选技能清单（逐个审核）

---

## English

A marketplace repository for reusable Agent skills.

### Purpose

- Curate reusable Agent Skills
- Provide a consistent structure, standards, and review workflow
- Focus on shared content (code + docs only)

### Admission Policy (active)

1. Candidate skills are proposed by the maintainer agent.
2. Every skill requires explicit owner approval.
3. Only approved skills can be moved into `skills/`.
4. Default workflow: direct push to `main`.

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
- `description` must clearly state trigger contexts.

### Current Status

- Marketplace skeleton initialized
- Candidate skills pending owner-by-owner approval
