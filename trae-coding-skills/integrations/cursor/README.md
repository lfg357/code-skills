# Cursor 集成指南

## 使用方式

1. 将 `_orchestrator.yml` 内容放入 Cursor 的 **Rules for AI**
2. 在 `.cursorrules` 文件中引用具体 Skill：

```
# .cursorrules
You are an expert software engineer following Trae Coding Skills.

## Active Skills
- karpathy-style: Clear, flat, explicit code
- minimal-coding: Essential implementation only
- test-driven: All changes must have tests

## Constraints
- Never assume business logic
- No over-engineering
- Every line must serve a purpose
```

3. 在 Chat 中使用 `@` 引用工作流模板文件
