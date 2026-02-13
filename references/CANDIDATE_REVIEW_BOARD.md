# Candidate Review Board（候选技能审核看板）

> 说明：这是“可读审核页”，用于在网站化之前统一查看候选技能状态。
> 入选硬门槛：通过安全审计（无 BLOCK）+ Owner 明确批准。

Last updated: 2026-02-13

---

## 审核状态定义

- `PENDING`：待审核
- `SECURITY_REVIEW`：安全审计中
- `READY_FOR_OWNER`：通过技术审核，待 Owner 最终批准
- `APPROVED`：已批准，可进入 `skills/`
- `REJECTED`：拒绝入库

---

## 候选池总览

| Skill | Category | Security | Compatibility | Real-world | Status | Notes |
|---|---|---:|---|---|---|---|
| post-to-wechat | Publishing | N/A | TBD | TBD | PENDING | 待正式提案与安全审计 |
| github-daily-report | Dev & GitHub | N/A | TBD | TBD | PENDING | 已有脚本原型，待提案化 |
| jimeng-image-gen-api | Content | N/A | TBD | TBD | PENDING | 已有实操流程，待规范化 |
| skill-security-audit | Ops & Security | 91 | Claude/OpenAI/Gemini/OpenClaw | true | APPROVED | 已升级为正式 skill |
| xiaohongshu-mcp-publishing-playbook | Publishing | 92 | OpenClaw(native), others(compatible) | true | APPROVED | 已入库为 `skills/xiaohongshu-mcp-publisher`，luyike221 路线已移除 |

---

## 详细评审记录

### 1) skill-security-audit

- 状态：`APPROVED`
- 安全分：`91`
- 关键证据：
  - `proposals/skill-security-audit/SECURITY-REPORT.md`
  - `skills/skill-security-audit/skill.json`
- 结论：可作为入库硬门槛执行器。

### 2) post-to-wechat

- 状态：`PENDING`
- 当前缺口：
  - 缺少标准化提案（按 `references/PROPOSAL_TEMPLATE.md`）
  - 缺少 `skill.json`
  - 缺少安全审计报告

### 3) github-daily-report

- 状态：`PENDING`
- 当前缺口：
  - 脚本与 skill 边界还未拆分
  - 缺少跨平台兼容标签与质量指标
  - 缺少安全审计报告

### 4) jimeng-image-gen-api

- 状态：`PENDING`
- 当前缺口：
  - 需要明确“付费前确认”规则为硬约束
  - 缺少标准化提案与安全报告
  - 缺少 `skill.json`

### 5) xiaohongshu-mcp-publishing-playbook

- 状态：`APPROVED`
- 提案：
  - `proposals/xiaohongshu-mcp-publishing-playbook/PROPOSAL.md`
- 正式技能：
  - `skills/xiaohongshu-mcp-publisher/`
- 结论：
  - 已按 owner 指令入库
  - 使用 `xiaohongshu-mcp` 路线
  - `luyike221` 路线已移除

---

## 下一步执行顺序（建议）

1. `github-daily-report`（已有实跑基础，最快形成标准样板）
2. `post-to-wechat`
3. `jimeng-image-gen-api`

> 规则不变：每个候选必须先过 `skill-security-audit`，再提交 Owner 批准。
