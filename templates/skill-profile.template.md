---
slug: your-skill-slug
name:
  zh: 技能中文名
  en: Skill English Name # 可选
summary:
  zh: 用一句话说明这个技能解决什么问题。
  en: One-line optional English summary. # 可选
source:
  type: local # local | external
  url: https://github.com/owner/repo # external 或有公开上游时填写
  local_path: skills/your-skill-slug # local 时必填
category:
  - 我想写代码/修 Bug
tags:
  - tag-1
  - tag-2
status: candidate # candidate | under_review | verified | deprecated | archived
quality_score: 0 # 内部评估
security_grade: C # A | B | C | D
install_complexity: medium # low | medium | high
last_verified_at: 2026-03-02
---

# 技能名称（中文）

> 一句话说明最适合谁，以及为什么值得安装。

## 快速判断

- 值不值得装：推荐安装 / 按场景安装 / 暂缓安装
- 最适合：一句话说清任务类型
- 来源：本地收录 / 外部来源 + 上游链接说明
- 安全：`A/B/C/D`，一句话说明风险边界
- 上手成本：`low / medium / high`，一句话说明依赖和准备成本

## 适合场景

- 场景 1
- 场景 2
- 场景 3

## 核心价值

1. 功能点 1：说明输入、输出和成功条件。
2. 功能点 2：说明为什么它比手工流程更快。
3. 功能点 3：说明边界，不要夸大能力。

## 最小上手

```bash
# 安装或拷贝步骤
```

安装后验证：

```bash
# 一个最小可运行命令
```

## 使用示例

基础示例：

```text
示例提示词或命令
```

进阶示例：

```text
示例提示词或命令
```

## 依赖与边界

- 运行依赖：`python3`、`node`、CLI 或服务地址
- 环境变量：`API_KEY`（如有）
- 网络访问：需要 / 可选 / 不需要
- 文件系统权限：读写哪些目录
- 敏感操作：是否涉及发布、删除、覆盖、外部写入

## 信任与维护

- 当前状态：`candidate / under_review / verified / deprecated / archived`
- 来源类型：`local / external`
- 上游来源：链接或说明无公开上游
- 维护者：`@handle`
- 最近验证日期：YYYY-MM-DD
- 兼容性：`Claude Code` / `OpenAI Agents` / `Gemini CLI` / `OpenClaw`

## 审核与反馈

- 审核结论：一句话说明目前是否建议安装
- 已审核评论：暂无，或指向 `comments/<slug>.yaml`
- 审核记录：`YYYY-MM-DD` 初审 / 复审结论
