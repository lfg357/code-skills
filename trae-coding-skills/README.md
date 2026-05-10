# Trae Coding Skills

一套高标准的 AI 辅助编码规范，适用于 Trae、Cursor、VS Code 等 AI IDE。

覆盖 **Python、C++、Java、Go、JavaScript/TypeScript、Rust** 等主流语言，杜绝擅自假设、过度设计、非必要修改、无目标编码。

---

## 🎯 设计理念

> **代码是写给人看的，顺便给机器执行。**

- **根因驱动**：Bug 修复必须找到根因，禁止掩盖症状
- **数据驱动**：性能优化必须有基准测试，禁止过早优化
- **最小可行**：只实现需求明确要求的功能，拒绝过度设计
- **显式优于隐式**：命名即文档，拒绝魔法

---

## 🚀 快速开始

### Trae 用户

1. 将 `core-skills/_orchestrator.yml` 的内容复制到 Trae 的 **System Prompt**
2. 根据当前任务，将对应 Skill（如 `bug-fix.yml`）复制到 **上下文**
3. 或直接复制 `workflow-templates/` 中的完整工作流

```bash
# 示例：新功能开发工作流
cat workflow-templates/new-feature.yml
```

### 其他 AI IDE（Cursor / VS Code Copilot）

参考 `integrations/` 目录下的对应配置说明。

---

## 📋 Skills 清单

| Skill | 优先级 | 触发场景 | 自动触发 |
|-------|--------|----------|----------|
| **Orchestrator** | Highest | 所有代码任务入口 | ✅ |
| **Karpathy Style** | High | 设计 / 实现 / API 定义 | ✅ |
| **Minimal Coding** | High | 实现 / 重构 / 简化 | ✅ |
| **Code Review** | High | 审查 / PR / Commit | ✅ |
| **Refactoring** | High | 重构 / 技术债务清理 | ❌ |
| **Bug Fix** | Highest | 修复 / Debug / 异常分析 | ✅ |
| **Optimization** | High | 性能调优 / 资源优化 | ❌ |
| **Test Driven** | High | 新增代码 / Bug 修复 / 重构 | ✅ |
| **Documentation** | Medium | 注释 / 文档 / 可读性 | ❌ |
| **Security Hardening** | High | 安全审查 / 输入处理 | ❌ |

---

## 🗂️ 仓库结构

```
trae-coding-skills/
├── core-skills/           # 核心编码技能（通用层）
├── language-modules/      # 语言特异性规则（叠加层）
├── workflow-templates/    # 预定义工作流（多 Skill 协同）
├── examples/              # Before / After 代码示例
├── integrations/          # 与具体 IDE 集成配置
└── tools/                 # 辅助工具脚本
```

### 核心技能（core-skills/）

通用编码规范，与语言无关：

- **`_orchestrator.yml`** — 全局触发判断与技能协同调度
- **`karpathy-style.yml`** — Karpathy 规范：清晰、扁平、显式
- **`minimal-coding.yml`** — 极简编码：最小可行实现
- **`code-review.yml`** — 系统性代码审查（Critical / Warning / Suggestion）
- **`refactoring.yml`** — 小步安全重构，行为保持不变
- **`bug-fix.yml`** — 根因驱动的最小化修复
- **`optimization.yml`** — 数据驱动的性能优化
- **`test-driven.yml`** — 测试驱动规范（新增）
- **`documentation.yml`** — 文档与注释规范（新增）
- **`security-hardening.yml`** — 深度安全规范（新增）

### 语言模块（language-modules/）

在通用规则基础上叠加语言惯用法：

- **`python.yml`** — Pythonic：typing、pathlib、dataclasses、asyncio
- **`cpp.yml`** — Modern C++：RAII、Smart Pointer、Rule of Five
- **`java.yml`** — Java：Stream API、Optional、Records
- **`go.yml`** — Go way：Error handling、Context、Interface
- **`javascript-typescript.yml`** — TS/JS：严格类型、ES2022+
- **`rust.yml`** — Rust：Ownership、生命周期、unsafe 规范

### 工作流模板（workflow-templates/）

预定义的多 Skill 协同流程：

| 模板 | 适用场景 | 涉及 Skills |
|------|----------|-------------|
| `new-feature.yml` | 从零实现功能 | karpathy + minimal + test-driven + review |
| `hotfix.yml` | 线上 Bug 热修复 | bug-fix + test-driven + review |
| `refactor.yml` | 技术债务清理 | review + refactoring + minimal + review |
| `performance-tuning.yml` | 性能调优 | review + optimization + benchmark |

---

## 🔄 典型工作流示例

### 场景 1：新功能开发

```
用户：帮我实现一个用户认证模块

Orchestrator 识别 → 触发 new-feature 工作流
  Step 1: karpathy-style   → 设计 API 签名（显式、扁平）
  Step 2: test-driven      → 编写失败的单元测试
  Step 3: minimal-coding   → 最小实现（通过测试）
  Step 4: code-review      → 审查输出问题列表
  Step 5: refactoring      → 简化复杂度（如需要）
  Step 6: documentation    → 补充关键注释
```

### 场景 2：Bug 修复

```
用户：这段代码在并发下偶尔崩溃

Orchestrator 识别 → 触发 hotfix 工作流
  Step 1: bug-fix          → 复现 → 根因分析 → 最小修复
  Step 2: test-driven      → 补充回归测试（并发场景）
  Step 3: code-review      → 验证无引入新问题
```

### 场景 3：纯概念问答（不触发任何 Skill）

```
用户：Python 的 GIL 是什么？

Orchestrator 识别为纯概念问答
  → 不触发任何 Skill
  → 仅提供概念解释，不输出代码
```

---

## ✅ 提交前自检

```bash
# 校验所有 Skill YAML 格式合规
python tools/validate-skills.py

# 生成指定工作流的复合 Prompt
python tools/generate-workflow.py workflow-templates/new-feature.yml

# 将 YAML Skill 渲染为易读 Markdown
python tools/render-markdown.py core-skills/bug-fix.yml
```

---

## 📄 License

[MIT](LICENSE)

---

## 🤝 Contributing

欢迎提交 Issue 和 PR！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解规范。

核心原则：
- 新增 Skill 必须有 `examples/` 下的 Before/After 示例
- 修改 Skill 必须更新 `CHANGELOG.md`
- 所有 YAML 必须通过 `tools/validate-skills.py` 校验
