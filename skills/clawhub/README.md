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

## 1. 适用场景

- 需要在线搜索并安装新 skills
- 需要批量更新本地已安装 skills
- 需要将本地 skill 发布到 clawhub registry

## 2. 核心功能

1. `search/install/update/list` 本地技能管理。
2. `publish` 将本地技能发布到 registry。
3. 支持版本指定和哈希匹配升级。

## 3. 最简安装（3 步）

```bash
npm i -g clawhub
mkdir -p .claude/skills
cp -r skills/clawhub .claude/skills/
```

## 4. 使用方式

```bash
clawhub search "postgres backups"
clawhub install my-skill
clawhub update --all
```

发布前认证：

```bash
clawhub login
clawhub whoami
```

## 5. 依赖与权限

- 运行依赖：`clawhub` CLI（npm）
- 网络访问：需要（registry/API）
- 敏感操作：发布命令会产生外部变更

## 6. 安全信息

- 安全等级：`A`
- 依据摘要：命令边界明确，可审计，流程可回溯

## 7. 维护状态

- 当前状态：`verified`
- 上游站点：`https://clawhub.ai`
- 维护者：`OpenClaw Agent`
- 最近验证日期：`2026-02-24T22:32:30Z`

## 8. 评论摘要（默认 3 条）

- 暂无已审核评论，详见 `comments/clawhub.yaml`

## 9. 审核记录

- `2026-02-24` 收录并通过复审
