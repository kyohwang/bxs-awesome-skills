# Contributing / 贡献指南

## 中文

### 收录硬规则

1. 新技能必须先进入 `proposals/`。
2. 必须通过 `skill-security-audit`（无 BLOCK）。
3. 必须由 Owner 明确批准。
4. 才能进入 `skills/`。

### 必需文件

- `SKILL.md`
- `skill.json`（兼容标签 + 质量指标）

### 命名规范

- 小写 + 连字符（kebab-case）
- 目录名与 skill 名一致

### 提交流程

1. 使用 `references/PROPOSAL_TEMPLATE.md` 新建提案
2. 写清楚：目标、输入输出、风险边界、安装方式
3. 跑安全审计并附 `SECURITY-REPORT`
4. 等 Owner 审核同意

## English

### Hard admission rules

1. New skills must start in `proposals/`.
2. Must pass `skill-security-audit` (no BLOCK findings).
3. Must receive explicit owner approval.
4. Only then can be promoted into `skills/`.

### Required files

- `SKILL.md`
- `skill.json` (compatibility + quality metrics)

### Naming

- lowercase kebab-case
- directory name must match skill name

### Submission flow

1. Create proposal from `references/PROPOSAL_TEMPLATE.md`
2. Declare objective, IO contract, risk boundaries, install method
3. Attach security report
4. Wait for owner approval
