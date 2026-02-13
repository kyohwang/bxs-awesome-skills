---
name: xiaohongshu-mcp-publisher
description: 使用 xiaohongshu-mcp HTTP 服务进行小红书发布。适用于“先审后发”的图文发布场景：先检查健康与登录状态，必要时取二维码登录，按 pages 目录生成 payload 给 owner 审核，收到“确认发送”后再调用 /api/v1/publish，并回传结果。
---

# xiaohongshu-mcp-publisher

按以下顺序执行，避免误发：

1. 健康检查
- `GET /health`
- 若失败，先报错，不进入发布。

2. 登录检查
- `GET /api/v1/login/status`
- 若 `is_logged_in=false`：调用 `GET /api/v1/login/qrcode` 获取二维码并发送给 owner，扫码后轮询登录状态 3-5 次。

3. 组装待发内容（先审）
- 从 `pages/<区间>/` 读取：`title.txt`、`content.txt`、`images_manifest.txt`、`publish.json`。
- 图片顺序严格按 `images_manifest.txt`。
- 按 owner 指令修改标题/正文（常见：只改正文第一行）。
- 输出完整待发内容给 owner 审核。

4. 审核门槛
- 只有收到 owner 明确“确认发送/发布”后才可调用发布接口。

5. 发布
- `POST /api/v1/publish`
- 成功条件：返回 `success=true` 且 `message`/`status` 为发布完成语义。
- 失败时返回原始错误，并建议优先检查登录态是否掉线。

6. 复核
- 若用户反馈“没看到”，先再次检查登录态并提示平台侧可能有审核/延迟。

## 约束
- 不使用 luyike221 路线（已移除）。
- 优先使用稳定可达的 `xiaohongshu-mcp` 服务端。
- 严格执行“先审后发”。
