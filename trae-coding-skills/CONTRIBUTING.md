# Contributing Guide

感谢你对 Trae Coding Skills 的贡献！

## 提交规范

### 新增 Skill

1. 在 `core-skills/` 下创建 `{skill-name}.yml`
2. 必须包含以下字段：
   - `skill`：Skill 标识名
   - `priority`：优先级（highest / high / medium / low）
   - `description`：一句话描述
   - `activation`：触发条件（`trigger_on` / `ignore_when`）
   - `principles`：核心原则
   - `constraints`：禁止行为
3. 在 `examples/{skill-name}/` 下创建 Before/After 示例
4. 更新 `README.md` Skills 清单
5. 更新 `CHANGELOG.md`

### 修改现有 Skill

1. 遵循 Semver：
   - 新增原则/规则 → Minor 版本
   - 修复描述/示例 → Patch 版本
   - 移除/重命名规则 → Major 版本
2. 在 `CHANGELOG.md` 中说明变更理由

### 代码示例规范

- 示例必须真实可运行（语法正确）
- Before 示例必须展示明确的反模式
- After 示例必须展示改进后的代码
- `notes.md` 必须逐条说明修改点及理由

## 本地校验

```bash
python tools/validate-skills.py
```

所有 YAML 必须通过校验后才能提交 PR。
