# SECURITY REPORT — skill-security-audit

- Date: 2026-02-12
- Scope: `proposals/skill-security-audit/PROPOSAL.md`
- Reviewer: OpenClaw Agent

## Verdict

**REVIEW**（可继续推进，但暂不建议直接上榜/入正式技能）

## Score

**82 / 100**

## Findings

### Positive

1. 明确了三层防线：静态规则 + 第三方扫描 + 官方基线映射。
2. 定义了 PASS/REVIEW/BLOCK 及一票否决，方向正确。
3. 要求证据与修复建议，具备可审计性。

### Risks / Gaps

1. **供应链约束不足（中风险）**
   - 提案依赖 `mcp-scan`，但未规定版本锁定、校验策略（hash/signature/source pinning）。
2. **执行隔离策略未落地（中风险）**
   - 未明确扫描执行环境（沙箱/容器/网络策略/最小权限）。
3. **规则抗绕过细节不足（中风险）**
   - 仅给了规则方向，未定义匹配方式（语义变体、编码混淆、分段拼接）。
4. **误报治理缺口（低~中风险）**
   - 提到白名单，但未定义审批链、时效、复核机制。

## Recommended Fixes (Before Promotion)

1. 固化第三方引擎版本：`mcp-scan` 版本锁定 + 安装源白名单 + 校验（至少 hash）。
2. 强制隔离执行：默认在受限环境运行审计（禁写系统目录、默认禁外网或域名白名单）。
3. 增加规则防绕过：对 base64/hex/分段拼接/同义替换做检测策略。
4. 增加“证据最小集”模板：文件路径、行号、命中规则ID、上下文片段。
5. 补齐白名单治理：谁能批准、有效期、自动过期、复核触发条件。

## Decision

- 当前状态：**REVIEW**
- 建议：修完上述 5 项后再进入 `skills/` 与榜单评审。
