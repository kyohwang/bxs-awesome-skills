---
name: turn-brain-teaser-publisher
description: 基于 /data/turn/AGENT.md 流程，把脑筋急转弯资源包解压并生成封面+题目页+答案页，再按 /data/pub/pages/<range>/ 标准结构产出可发布内容。适用于“收到题图压缩包后，批量生成一组区间内容并交付发布目录”的任务。
---

# turn-brain-teaser-publisher

## 目标
将用户提供的题图压缩包处理为可发布目录：
- 输入：`/data/turn/<range>/content.txt` + `序号.png` 题图
- 生成：问题图、答案图、拼接页图、封面
- 输出：`/data/pub/pages/<range>/`（含 `title.txt`、`content.txt`、`images_manifest.txt`、`publish.json`、`post.md`、`images/`）

## 固定前提
- 主流程根目录：`/data/turn`
- 以 `/data/turn/AGENT.md` 为准
- 输出统一落盘：`/data/pub/pages`

## 标准流程
1. 解压用户资源包到 `/data/turn`（保持区间目录，如 `41~50`）
2. 校验输入完整性：
   - 存在 `content.txt`
   - 每行格式：`序号.问题文案 答案：答案文案`
   - 对应 `序号.png` 存在
3. 执行页面生成：
   - `node /data/turn/generate_qa_pages.js --range-dir "<range>"`
4. 生成封面：
   - `python3 /data/turn/cover.py --bg /data/turn/data_cover.jpg --range <range> --out /data/turn/<range>/output/final_cover.jpg`
5. 组装发布目录：`/data/pub/pages/<range>/`
   - `images/01_cover.jpg` = `final_cover.jpg`
   - `images/02_<n>.jpg ...` 依次放 `output/page/*.jpg`
   - 同步生成：
     - `title.txt`
     - `content.txt`
     - `images_manifest.txt`
     - `publish.json`
     - `post.md`
6. 先输出完整待发内容给 owner 审核，再发布。

## 文件命名规范（发布目录）
- 标题：`幼儿脑筋急转弯：<range>`（可按 owner 指令覆盖）
- 图片清单：严格按序号输出，封面永远第一张
- `publish.json` 字段：`title`、`content`、`images[]`、`tags[]`

## 失败处理
- 缺图/格式错误：停止并给出缺失序号清单
- 生成脚本报错：返回原始 stderr + 建议修复项
- 只要产物不完整，不写入 `/data/pub/pages/<range>`

## 来源说明
- 流程依据：`/data/turn/AGENT.md`
- 该技能是流程编排，不替代上游脚本能力
