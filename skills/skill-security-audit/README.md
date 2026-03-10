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

> 收录前先做安全准入；需要可追溯证据链时，这是最先应该装的技能之一。

## 快速判断

- 值不值得装：推荐安装。任何准备进入 `skills/` 的候选 skill 都应先过这一关。
- 最适合：安全准入、周期复审、需要路径和行号证据的审计场景。
- 来源：本地收录，无额外服务依赖，规则和输出结构都可直接审阅。
- 安全：`A`，默认做静态扫描，不破坏目标目录。
- 上手成本：`low`，只需要 `python3`，可选 `bash`。

## 适合场景

- 提案技能进入 `skills/` 前的安全准入检查
- 已收录技能的周期性复审
- 需要输出可追溯证据链的审核流程

## 核心价值

1. 静态规则扫描可以快速定位高风险模式，而不是只靠人工目检。
2. 统一输出 `PASS / REVIEW / BLOCK`，方便直接接入审核流程或 CI。
3. 报告包含证据路径、行号和修复建议，便于人工复核和回归对比。

## 最小上手

```bash
mkdir -p .claude/skills
cp -r skills/skill-security-audit .claude/skills/
python3 skills/skill-security-audit/scripts/skill_security_audit.py --help
```

安装后验证：

```bash
python3 scripts/skill_security_audit.py <target_dir> --out SECURITY-REPORT.generated.json
```

## 使用示例

基础用法：

```bash
python3 scripts/skill_security_audit.py <target_dir> --out SECURITY-REPORT.generated.json
```

可选 MCP 扫描：

```bash
bash scripts/run_mcp_scan.sh <target_dir> mcp-scan-report.json
```

## 依赖与边界

- 运行依赖：`python3`、`bash`（可选）
- 环境变量：无强制项
- 网络访问：默认不需要
- 文件系统权限：读取目标目录，写入审计报告
- 敏感操作：不会修改目标 skill 目录内容

## 信任与维护

- 当前状态：`verified`
- 来源类型：`local`
- 审计方式：规则透明，输出结构固定，可追溯证据完整
- 维护者：`OpenClaw Agent`
- 最近验证日期：`2026-02-13`
- 兼容性：`Claude Code(native)`、`OpenAI Agents(compatible)`、`Gemini CLI(compatible)`、`OpenClaw(native)`

## 审核与反馈

- 审核结论：建议作为所有候选 skill 的默认准入检查器。
- 已审核评论：暂无，见 `comments/skill-security-audit.yaml`
- 审核记录：`2026-02-13` 初次收录并通过安全审计
