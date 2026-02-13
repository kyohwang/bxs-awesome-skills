# bxs-awesome-skills

[中文](#中文) | [English](#english)

---

## 中文

**The most reliable curated skills armory for agents.**

这是一个给 Agent 用的 **Skills 兵器谱**。

灵感来自《兵器谱》：江湖不缺兵器，缺的是靠谱兵器。  
这个仓库不追求“收得多”，而追求“收得准”：
- 分门别类
- 安全靠谱（硬门槛）
- 真实有效

## 你现在就能用（安装优先）

### 方式 A：直接复制 skill 目录

```bash
# 示例：安装 skill-security-audit 到个人 Claude skills
mkdir -p ~/.claude/skills
cp -r skills/skill-security-audit ~/.claude/skills/
```

### 方式 B：项目级安装（推荐团队）

```bash
mkdir -p .claude/skills
cp -r skills/skill-security-audit .claude/skills/
```

> 每个 skill 的具体安装方式，见 `skills/index.json` 的 `install` 字段。

## 收录流程（标准化）

统一采用：

`proposal -> security-audit -> owner approve -> skills/`

详细规范：
- `references/CONTRIBUTING.md`
- `references/PROPOSAL_TEMPLATE.md`

## 跨平台兼容标签

每个 skill 必须声明兼容标签（`compatibility`）：
- `claude-code`
- `openai-agents`
- `gemini-cli`
- `openclaw`

并标注等级：
- `native`（官方原生）
- `compatible`（可适配）
- `partial`（部分支持）
- `none`（不支持）

结构定义见：`references/SKILL_MANIFEST.schema.json`

## 质量指标（公开）

每个 skill 必须公开：
- `security_score`（安全分）
- `real_world_validated`（是否实战验证）
- `maintainer`（维护人）
- `last_verified_at`（最近验证时间）

同样写入 `skills/index.json` 和各 skill 的 `skill.json`，便于后续榜单化。

## 仓库定位

- 技能市场仓库（内容共享为主）
- 排行榜是能力层，不是目的本身
- 无实战价值技能不入库

## 排名维度（未来榜单）

- **有效性**：是否稳定解决真实问题
- **安全性**：是否遵循最小权限、可审计、可回滚
- **可复用性**：是否能跨项目重复使用
- **可维护性**：结构是否清晰，依赖是否可控
- **实战反馈**：是否有真实使用记录与结果

## 分类体系

- 内容生产（Content）
- 发布分发（Publishing）
- 自动化流程（Automation）
- 开发协作（Dev & GitHub）
- 数据与研究（Data & Research）
- 运维与安全（Ops & Security）

## 目录结构

```text
skills/           # 已审核通过的正式技能
skills/_template/ # 技能模板
proposals/        # 待审核候选技能说明
references/       # 规范与参考文档
scripts/          # 辅助脚本
```

---

## English

**The most reliable curated skills armory for agents.**

A marketplace repository for reusable, production-grade agent skills.

This repository optimizes for quality over quantity:
- clear taxonomy
- security as a hard gate
- real-world effectiveness

## Install-first usage

### Option A: copy into personal skills

```bash
mkdir -p ~/.claude/skills
cp -r skills/skill-security-audit ~/.claude/skills/
```

### Option B: project-local install

```bash
mkdir -p .claude/skills
cp -r skills/skill-security-audit .claude/skills/
```

> Per-skill install instructions are tracked in `skills/index.json`.

## Admission pipeline (standardized)

`proposal -> security-audit -> owner approve -> skills/`

See:
- `references/CONTRIBUTING.md`
- `references/PROPOSAL_TEMPLATE.md`

## Cross-platform compatibility labels

Every skill must declare compatibility for:
- `claude-code`
- `openai-agents`
- `gemini-cli`
- `openclaw`

with levels:
- `native`
- `compatible`
- `partial`
- `none`

Schema: `references/SKILL_MANIFEST.schema.json`

## Public quality metrics

Every skill must publish:
- `security_score`
- `real_world_validated`
- `maintainer`
- `last_verified_at`

Stored in both per-skill `skill.json` and root `skills/index.json`.

## Positioning

- marketplace-first, content-sharing oriented
- leaderboard is an output, not the goal
- no proven value, no admission
