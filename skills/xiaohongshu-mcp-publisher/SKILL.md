---
name: xiaohongshu-mcp-publisher
description: 使用 xiaohongshu-mcp HTTP 服务执行小红书图文发布。适用于“先审后发”流程：健康检查、登录检查/二维码登录、按 pages 目录组装内容、owner 审核后发布、回传结果与失败诊断。
---

# xiaohongshu-mcp-publisher

## 来源与作者
- 上游项目：`xiaohongshu-mcp`
- 作者仓库地址：`https://github.com/xpzouying/xiaohongshu-mcp`
- 本技能定位：对上游能力做发布流程编排（不是替代上游项目）

## 功能
1. 服务可用性检查（health）
2. 登录态检查（login/status）
3. 二维码登录（login/qrcode）
4. 按目录规范组装发布内容（pages/<区间>）
5. 发布前审查（先发给 owner 确认）
6. 调用发布接口（/api/v1/publish）
7. 失败诊断与重试建议（优先检查登录是否掉线）

## 使用说明（标准流程）

### 第 1 步：检查服务
- `GET /health`
- 不健康则停止并报错，不进入发布。

### 第 2 步：检查登录
- `GET /api/v1/login/status`
- 若 `is_logged_in=false`：
  - 调 `GET /api/v1/login/qrcode` 获取二维码
  - 发给 owner 扫码
  - 扫码后轮询 3-5 次 `login/status`，直到稳定 `true`

### 第 3 步：组装待发内容（先审）
从 `pages/<区间>/` 读取：
- `title.txt`
- `content.txt`
- `images_manifest.txt`
- `publish.json`

规则：
- 图片顺序严格按 `images_manifest.txt`
- 按 owner 指令改标题/正文（常见：只改正文首行）
- 先完整输出待发内容给 owner 审核

### 第 4 步：审核门槛
- 只有收到 owner 明确“确认发送/发布”后才允许调用发布接口

### 第 5 步：发布
- `POST /api/v1/publish`
- 成功判定：`success=true` 且 `message/status` 显示发布完成语义

### 第 6 步：复核
- 若用户反馈“没看到”，先查登录态是否掉线
- 同时提示平台可能存在审核/展示延迟

## 请求示例（结构）
```json
{
  "title": "示例标题",
  "content": "示例正文",
  "images": ["/path/img1.jpg", "/path/img2.jpg"],
  "tags": ["幼儿", "亲子互动"]
}
```

## 约束
- `luyike221` 路线已移除，不再使用
- 优先使用稳定可达的 `xiaohongshu-mcp` 服务
- 严格执行“先审后发”
