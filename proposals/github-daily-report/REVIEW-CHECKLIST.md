# github-daily-report 复审清单

状态目标：`under_review -> verified`

## 1. 安全与权限

- [ ] 重新运行 `skill-security-audit`，无 BLOCK 发现
- [ ] 补齐最新 `SECURITY-REPORT.generated.json`
- [ ] 确认 `GITHUB_TOKEN` 仅最小权限（只读仓库元数据）
- [ ] 确认 SQLite 路径与写入范围可控，不覆盖系统关键目录

## 2. 可用性验证

- [ ] `collect` 命令可正常执行并写入快照
- [ ] `report` 命令可正常输出三段式日报
- [ ] 输出稳定包含：总榜/增长榜/新锐榜 三段
- [ ] 每段默认 10 条，异常时有明确提示

## 3. 数据与质量

- [ ] 24h 增长计算逻辑复核（边界：缺失历史样本）
- [ ] 去重策略有效（避免同仓库高频重复霸榜）
- [ ] 示例输出已更新到 `TEST-REPORT.md`

## 4. 元数据回填

- [ ] 更新 `skills/github-daily-report/skill.json` 的 `last_verified_at`
- [ ] 更新 `skills/index.json` 对应字段
- [ ] 更新 `catalog/skills.yaml` 对应字段（状态、分级、验证时间）

## 5. 发布前门槛

- [ ] Owner 复核通过
- [ ] 评论摘要（如有）已同步到 `comments/github-daily-report.yaml`
- [ ] 复审结论记录到本文件底部

---

复审结论（待填写）：

- 日期：
- 审核人：
- 结论：
- 备注：
