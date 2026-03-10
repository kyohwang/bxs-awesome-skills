---
slug: xiaohongshu-mcp-publisher
name:
  zh: 小红书 MCP 发布助手
  en: Xiaohongshu MCP Publisher
summary:
  zh: 覆盖健康检查、登录检查、先审后发的小红书发布流程技能。
  en: Publish workflow skill for xiaohongshu-mcp with review-before-send gates.
source:
  type: local
  url: https://github.com/xpzouying/xiaohongshu-mcp
  local_path: skills/xiaohongshu-mcp-publisher
category:
  - 我想做内容与设计
  - 我想自动执行任务
tags:
  - xiaohongshu
  - publishing
  - mcp
status: verified
quality_score: 82
security_grade: A
install_complexity: medium
last_verified_at: 2026-02-13T10:31:39Z
---

# 小红书 MCP 发布助手

> 当你要做“小红书内容先审后发”，而且希望把登录、诊断和发布边界固定下来时，它很有价值。

## 快速判断

- 值不值得装：推荐安装。适合对发布流程有审核要求的内容团队。
- 最适合：图文内容编排、登录检查、发布前复核和失败诊断。
- 来源：本地收录，公开上游为 `https://github.com/xpzouying/xiaohongshu-mcp`。
- 安全：`A`，强制先审后发；真正的外部变更只发生在发布确认后。
- 上手成本：`medium`，需要可访问 `xiaohongshu-mcp` 服务并准备登录态。

## 适合场景

- 小红书图文内容需要先审后发时
- 批量按目录规范组装发布内容时
- 发布失败后需要标准化诊断和重试建议时

## 核心价值

1. 把健康检查、登录检查、内容组装和发布确认串成固定流程，减少漏步。
2. 发布动作被明确放在最后一步，降低误发风险。
3. 失败时能回到统一诊断入口，而不是靠临时排查。

## 最小上手

```bash
mkdir -p .claude/skills
cp -r skills/xiaohongshu-mcp-publisher .claude/skills/
# 按 SKILL.md 完成服务地址与登录准备
```

安装后验证：

```bash
curl -s <service_base>/health
```

## 使用示例

标准流程：

```text
1. GET /health
2. GET /api/v1/login/status
3. 必要时 GET /api/v1/login/qrcode
4. 审核内容后 POST /api/v1/publish
```

发布前检查：

```text
先确认登录状态、内容目录和 owner 明确授权，再执行 publish。
```

## 依赖与边界

- 运行依赖：可访问 `xiaohongshu-mcp` HTTP 服务
- 环境变量：按部署方式决定
- 网络访问：需要
- 文件系统权限：读取 `pages/<区间>/` 内容文件
- 敏感操作：会对外平台发布内容，必须 owner 明确确认

## 信任与维护

- 当前状态：`verified`
- 来源类型：`local`，公开上游为 `xpzouying/xiaohongshu-mcp`
- 维护者：`OpenClaw Agent`
- 最近验证日期：`2026-02-13`
- 兼容性：`Claude Code(compatible)`、`OpenAI Agents(compatible)`、`Gemini CLI(compatible)`、`OpenClaw(native)`

## 审核与反馈

- 审核结论：推荐给有明确审核边界的内容发布流程使用。
- 已审核评论：暂无，见 `comments/xiaohongshu-mcp-publisher.yaml`
- 审核记录：`2026-02-13` 收录并完成安全审计
