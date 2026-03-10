---
slug: clawhub
name:
  zh: ClawHub CLI 技能
  en: ClawHub CLI
summary:
  zh: 使用 clawhub CLI 进行技能搜索、安装、更新和发布。
  en: Search, install, update, and publish skills via clawhub CLI.
source:
  type: local
  url: https://clawhub.ai
  local_path: skills/clawhub
category:
  - 我想自动执行任务
  - 我想做协作与办公
tags:
  - clawhub
  - registry
  - cli
status: verified
quality_score: 90
security_grade: A
install_complexity: medium
last_verified_at: 2026-02-24T22:32:30Z
---

# ClawHub CLI 技能

> 想快速发现、安装和发布 skill 时，它通常是最直接的入口。

## 快速判断

- 值不值得装：推荐安装。适合已经把 skill 当成工作流基础设施来用的团队。
- 最适合：搜索新 skill、批量更新本地 skill、发布自定义 skill。
- 来源：本地收录，公开上游为 `https://clawhub.ai`。
- 安全：`A`，常用命令边界清晰；`publish` 属于外部写操作。
- 上手成本：`medium`，需要全局安装 CLI 和网络访问。

## 适合场景

- 需要在线搜索并安装新 skills
- 需要批量更新本地已安装 skills
- 需要将本地 skill 发布到 clawhub registry

## 核心价值

1. 把 `search / install / update / publish` 放到一个统一 CLI 里，减少切换成本。
2. 对技能分发、升级和版本管理更友好，适合团队化使用。
3. 发布流程相对标准化，方便把本地 skill 推到 registry。

## 最小上手

```bash
npm i -g clawhub
mkdir -p .claude/skills
cp -r skills/clawhub .claude/skills/
```

安装后验证：

```bash
clawhub search "postgres backups"
```

## 使用示例

搜索与安装：

```bash
clawhub search "postgres backups"
clawhub install my-skill
```

更新与认证：

```bash
clawhub update --all
clawhub login
clawhub whoami
```

## 依赖与边界

- 运行依赖：`clawhub` CLI（npm）
- 环境变量：无强制项
- 网络访问：需要，依赖 registry/API
- 文件系统权限：会管理本地 skills 安装目录
- 敏感操作：`publish` 会对外发布内容，需人工确认

## 信任与维护

- 当前状态：`verified`
- 来源类型：`local`，公开上游为 `https://clawhub.ai`
- 维护者：`OpenClaw Agent`
- 最近验证日期：`2026-02-24`
- 兼容性：`Claude Code(compatible)`、`OpenAI Agents(compatible)`、`Gemini CLI(compatible)`、`OpenClaw(native)`

## 审核与反馈

- 审核结论：推荐作为团队级 skill 发现和分发入口使用。
- 已审核评论：暂无，见 `comments/clawhub.yaml`
- 审核记录：`2026-02-24` 收录并通过复审
