# xiaohongshu-mcp-publishing-playbook 提案（候选）

## 1) Basic Info
- Skill name: `xiaohongshu-mcp-publishing-playbook`
- Category: Publishing
- Owner: kyohwang

## 2) What problem it solves
- One-sentence positioning: 将“小红书 MCP 发布”从反复踩坑变成可复用 SOP（登录、校验、发布、回执）。
- Target users/scenarios: 需要批量发布图文、并希望可审计/可复现的自动化团队。

## 3) Inputs / Outputs
- Inputs:
  - 帖子目录（title/content/images/tags）
  - 发布策略（是否允许空标题、图片上限、发布前审查）
- Outputs:
  - 可执行发布 payload
  - 发布结果（成功/失败、错误原因、重试建议）
  - 操作证据（日志与关键截图）
- Failure behavior:
  - 登录失败时返回可重试步骤（重新取码、会话清理、状态轮询）
  - 校验失败时明确指出字段和限制来源（代码行）

## 4) Install & Usage
- Install command/path:
  - 候选阶段：文档型 skill（先不发布脚本）
- Invocation examples:
  - “读取 /data/pub/pages/21~30，先输出待发送内容给 owner 审核，确认后发布。”
  - “如遇校验错误，定位源码限制并按 owner 规则修改后重试。”

## 5) Security & Risk Boundary
- Required permissions:
  - 读取帖子目录、调用本地 xhs-mcp HTTP 接口、写本地日志。
- External side effects:
  - 真实发布会写入小红书账号内容（高影响外部动作）。
- Data handling policy:
  - cookie/token 仅本地使用，不落库到仓库。
  - 发布前必须 owner 明确“确认发送”。

## 6) Compatibility Labels
- claude-code: compatible
- openai-agents: compatible
- gemini-cli: compatible
- openclaw: native

## 7) Quality Metrics (initial)
- security_score: N/A（待安全审计）
- real_world_validated: true
- maintainer: kyohwang
- last_verified_at: 2026-02-13

## 8) Evidence
- security report path:
  - 待补：`proposals/xiaohongshu-mcp-publishing-playbook/SECURITY-REPORT.md`
- demo/test proof:
  - 已完成真实链路验证：二维码登录、状态轮询、图文发布（含规则调整后成功）。

---

## 实战经验总结（可沉淀为 skill 规则）

1. **常见报错与修复优先级**
   - `ImportError: Using SOCKS proxy, but the 'socksio' package is not installed`
     - 方案A：安装 `httpx[socks]`
     - 方案B：代码端 `httpx.AsyncClient(..., trust_env=False)`，默认不继承系统代理。

2. **二维码登录链路的关键稳定点**
   - 避免双初始化并发（会导致二维码接口偶发卡住/状态错乱）。
   - 获取二维码后启动单一路径等待登录，并在成功后立刻持久化 cookies。

3. **无图形环境（无 DISPLAY）处理**
   - 服务端必须走 `headless=true`，否则 Playwright 会报 `Missing X server or $DISPLAY`。

4. **发布前审查必须是硬规则**
   - 先输出完整 payload（标题/正文/图片顺序/标签）给 owner。
   - 收到“确认发送”后才调用发布接口。

5. **平台限制不要靠猜，必须以源码/接口校验为准**
   - 实战中发现第三方实现将图片上限硬编码为 9；按 owner 要求修成 17 后成功发布。
   - 标题校验同理：可按 owner 规则允许空标题，但要显式记录为“本地策略改动”。

6. **目录化发布规则（/data/pub/pages）**
   - 读取 `title.txt/content.txt/images_manifest.txt/publish.json`。
   - 图片顺序严格按 manifest，正文支持“仅替换首句”这类精细改写。

---

## 来源声明（非原创必填）

- Upstream repository: `xpzouying/xiaohongshu-mcp`
- 本提案类型: 经验封装与流程治理（非上游官方功能说明）
- 版本/提交: 待补（落库前补齐 commit SHA）
- License: 待补（落库前补齐）
- 说明：`luyike221` 路线已移除，不再作为本技能实现基础。
