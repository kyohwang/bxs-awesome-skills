---
slug: skill-security-audit
name:
  zh: Skill 安全审计
  en: Skill Security Audit
summary:
  zh: 对候选技能执行安全审计，输出 PASS/REVIEW/BLOCK。
  en: Security audit for candidate skills with deterministic verdicts.
source:
  type: local
  url: null
  local_path: skills/skill-security-audit
category:
  - 我关心安全与系统管理
tags:
  - security
  - audit
  - governance
status: verified
quality_score: 88
security_grade: A
install_complexity: low
last_verified_at: 2026-02-13T01:35:00Z
---

# Skill 安全审计

## 1. 适用场景

- 提案技能进入 `skills/` 前的安全准入检查
- 已收录技能的周期性复审
- 需要输出可追溯证据链（路径/行号/修复建议）的审计场景

## 2. 核心功能

1. 静态规则扫描并输出风险清单。
2. 根据规则生成统一结论：`PASS / REVIEW / BLOCK`。
3. 输出结构化报告，便于 CI 或人工复核。

## 3. 最简安装（3 步）

```bash
mkdir -p .claude/skills
cp -r skills/skill-security-audit .claude/skills/
python3 skills/skill-security-audit/scripts/skill_security_audit.py --help
```

## 4. 使用方式

基础用法：

```bash
python3 scripts/skill_security_audit.py <target_dir> --out SECURITY-REPORT.generated.json
```

可选 MCP 扫描：

```bash
bash scripts/run_mcp_scan.sh <target_dir> mcp-scan-report.json
```

## 5. 依赖与权限

- 运行依赖：`python3`、`bash`（可选）
- 环境变量：无强制项
- 网络访问：静态审计默认不需要
- 文件系统权限：读取目标目录，写入报告文件
- 敏感操作：无破坏性写入目标目录行为

## 6. 安全信息

- 安全等级：`A`
- 依据摘要：规则透明、证据可追溯、默认严格模式

## 7. 维护状态

- 当前状态：`verified`
- 维护者：`OpenClaw Agent`
- 最近验证日期：`2026-02-13T01:35:00Z`

## 8. 评论摘要（默认 3 条）

- 暂无已审核评论，详见 `comments/skill-security-audit.yaml`

## 9. 审核记录

- `2026-02-13` 初次收录并通过安全审计
