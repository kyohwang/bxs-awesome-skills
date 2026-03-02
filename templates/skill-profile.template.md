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
  url: https://github.com/owner/repo # external 时必填
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

> 可选英文名：Skill English Name

## 1. 适用场景

- 场景 1
- 场景 2
- 不适用场景（边界）

## 2. 核心功能

1. 功能点 1：说明输入与输出。
2. 功能点 2：说明成功条件。
3. 功能点 3：说明限制条件。

## 3. 最简安装（优先 3 步）

```bash
# Step 1
# Step 2
# Step 3
```

安装后最小验证：

```bash
# 一个最小可运行命令
```

## 4. 使用方式

基础示例：

```text
示例提示词或命令
```

进阶示例：

```text
示例提示词或命令
```

## 5. 依赖与权限

- 运行依赖：`curl`、`node`、`python` 等
- 环境变量：`API_KEY`（如有）
- 网络访问：是否需要
- 文件系统权限：读/写哪些目录
- 敏感操作：是否涉及删除、覆盖、外部发布

## 6. 安全信息（前台仅展示等级）

- 安全等级：`A/B/C/D`
- 评分依据摘要：
  - 权限最小化：通过/待改进
  - 安装可审计性：通过/待改进
  - 外部依赖可信度：通过/待改进
  - 敏感操作确认：通过/待改进

## 7. 维护状态

- 当前状态：`candidate / under_review / verified / deprecated / archived`
- 上游仓库：链接
- 最近上游提交：YYYY-MM-DD
- 最近验证日期：YYYY-MM-DD
- 维护者：`@handle`

## 8. 评论摘要（默认展示 3 条）

> 完整讨论见 GitHub Discussions 对应主题。

1. `[worth_installing]` 评论摘要 1（链接）
2. `[worth_installing_with_setup]` 评论摘要 2（链接）
3. `[wait_and_see]` 评论摘要 3（链接）

## 9. 审核记录

- `YYYY-MM-DD` 初审：`@reviewer`，结论：通过/退回
- `YYYY-MM-DD` 复审：`@reviewer`，结论：通过/退回

## 10. 变更记录

- `v0.1`：初版页面建立

