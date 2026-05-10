# Trae 集成指南

## 快速配置

### 1. 全局系统提示（System Prompt）

将 `core-skills/_orchestrator.yml` 的内容复制到 Trae 的 **AI 助手设置 → System Prompt** 中。

### 2. 上下文技能注入

根据当前任务，将对应 Skill 文件内容复制到对话上下文中：

- 写新功能 → `karpathy-style.yml` + `minimal-coding.yml` + `test-driven.yml`
- 审查代码 → `code-review.yml`
- 修复 Bug → `bug-fix.yml` + `test-driven.yml`
- 性能优化 → `optimization.yml`

### 3. 使用工作流模板

直接复制 `workflow-templates/` 中的 YAML 内容作为任务指令，AI 将按步骤执行。

## 设置片段

见 `settings-snippet.json`，可直接导入 Trae 配置。
