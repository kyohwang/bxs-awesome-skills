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

## 评分模型（已确认）

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

---

## 修复后补充策略（本次新增）

### 1) 第三方引擎供应链锁定（新增，强制）

- `mcp-scan` 固定版本（例如 `0.4.x`），禁止 `latest` 直装。
- 安装源固定为 PyPI 官方源（或你指定镜像白名单）。
- 记录依赖校验信息（至少 requirements lock + sha256）。
- 扫描报告中写入：`engine_version` / `engine_source` / `engine_hash`。

### 2) 扫描执行隔离（新增，强制）

默认在受限环境执行审计：
- 禁写系统目录（只允许工作目录临时文件）
- 网络默认关闭；仅在需要时开白名单域名
- 不继承宿主敏感环境变量（token/cookie）
- 执行用户最小权限（非 root）

### 3) 抗绕过检测（新增）

新增混淆检测规则：
- base64/hex 编码后拼接执行
- 分段字符串拼接高危命令
- 同义替换绕过（如下载执行链的变体）
- 隐蔽解释执行（`eval`, `exec`, 动态反射装载）

### 4) 证据最小集模板（新增，强制）

每条命中必须包含：
- `rule_id`
- `severity`
- `file_path`
- `line_start` / `line_end`
- `evidence_snippet`（脱敏后）
- `fix_hint`

### 5) 白名单治理机制（新增，强制）

- 白名单必须由 Owner 明确批准
- 每条白名单有 `reason` + `scope` + `expired_at`
- 默认 30 天过期，过期自动失效
- 每次命中白名单仍写入报告（可审计）

---

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
- `scripts/run_mcp_scan.sh`（引擎桥接，固定版本 + 校验）
- `references/whitelist-policy.md`（白名单治理）
- `references/evidence-schema.json`（证据结构）

## 后续增强（v2）

- CI 集成（PR 自动跑审计）
- 历史评分趋势
- 误报统计与规则回测
