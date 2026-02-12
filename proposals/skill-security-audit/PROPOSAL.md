# skill-security-audit 提案（待你最终批准后实施）

## 目标

为所有候选 Skill 提供统一安全审计，防止恶意 Skill 入库。

输出：`PASS / REVIEW / BLOCK` + 风险分（0-100）+ 证据 + 修复建议。

## 审计分层

1. **静态规则层（本地）**
   - 扫描 `SKILL.md` / `scripts/` / `references/` / `assets/`
   - 命中高危规则直接 `BLOCK`

2. **引擎层（第三方成熟方案）**
   - 默认调用 `mcp-scan --skills`
   - 合并其结果到统一报告

3. **官方基线策略层**
   - Anthropic / OpenAI / Google 官方安全实践映射
   - 最小权限、显式批准、注入防护、输出护栏

## 评分模型（你已同意）

- 总分 100
- 准入阈值：`>= 85`
- 任何 BLOCK 级问题：一票否决

建议权重：
- 权限与越权风险：25
- Prompt 注入与社工诱导：20
- 数据泄露与密钥处理：20
- 供应链与依赖安全：15
- 可审计与可回滚性：10
- 来源可信与维护状态：10

## 规则清单（首版）

### BLOCK（直接拒绝）
- 指令诱导绕过系统/安全规则
- 明示执行高危命令（如 `curl|bash`, `rm -rf /`, 任意 sudo 批量操作）
- 明文外传 token/cookie/私钥
- 隐蔽远程下载并执行

### REVIEW（人工复核）
- 需要广泛网络访问但无理由说明
- 写系统敏感路径或修改全局配置
- 依赖未锁版本且来源不明
- 说明文档与脚本行为不一致

### PASS（可入榜候选）
- 无 BLOCK
- 分数 >= 85
- 有最小权限说明与边界声明
- 有可复现测试与失败回滚说明

## 输出格式（短句版）

- 结论：PASS / REVIEW / BLOCK
- 总分：xx/100
- 高危项：N
- 关键证据：文件+行号
- 修复建议：最多 5 条，可执行

## 与仓库流程对接

1. 新 Skill 进入 `proposals/`
2. 跑 `skill-security-audit`
3. 结果归档到 `proposals/<skill>/SECURITY-REPORT.md`
4. 你确认后才允许进入 `skills/`

## 首版实现交付（仅提案，不入库）

- `scripts/skill_security_audit.py`（审计主程序）
- `references/security-rules.yaml`（规则库）
- `references/security-baseline-mapping.md`（官方实践映射）
- `scripts/run_mcp_scan.sh`（可选引擎桥接）

## 后续增强（v2）

- CI 集成（PR 自动跑审计）
- 历史评分趋势
- 误报豁免白名单（需你签字）
