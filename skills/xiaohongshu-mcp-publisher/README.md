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

## 1. 适用场景

- 小红书图文内容需要“先审后发”时
- 批量按目录规范组装发布内容时
- 发布失败后需要标准化诊断和重试建议时

## 2. 核心功能

1. 服务健康检查 + 登录态检查。
2. 二维码登录与状态轮询。
3. 读取 `pages/<区间>/` 内容，按规范生成发布请求。
4. Owner 明确确认后调用发布接口。

## 3. 最简安装（3 步）

```bash
mkdir -p .claude/skills
cp -r skills/xiaohongshu-mcp-publisher .claude/skills/
# 按 SKILL.md 完成服务地址与登录准备
```

## 4. 使用方式

标准流程：

1. `GET /health`
2. `GET /api/v1/login/status`
3. 必要时 `GET /api/v1/login/qrcode`
4. 审核内容后 `POST /api/v1/publish`

## 5. 依赖与权限

- 运行依赖：可访问 `xiaohongshu-mcp` HTTP 服务
- 网络访问：需要
- 文件系统权限：读取 `pages/<区间>/` 内容文件
- 敏感操作：外部平台发布（必须 owner 明确确认）

## 6. 安全信息

- 安全等级：`A`
- 依据摘要：强制先审后发、登录状态校验、流程边界清晰

## 7. 维护状态

- 当前状态：`verified`
- 上游仓库：`https://github.com/xpzouying/xiaohongshu-mcp`
- 维护者：`OpenClaw Agent`
- 最近验证日期：`2026-02-13T10:31:39Z`

## 8. 评论摘要（默认 3 条）

- 暂无已审核评论，详见 `comments/xiaohongshu-mcp-publisher.yaml`

## 9. 审核记录

- `2026-02-13` 收录并完成安全审计
