#!/usr/bin/env python3
"""将 YAML Skill 渲染为易读 Markdown。"""

import yaml
import sys
import pathlib
from typing import Any


def render_value(value: Any, indent: int = 0) -> str:
    """递归渲染值为 Markdown。"""
    prefix = "  " * indent

    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            if isinstance(v, (dict, list)):
                lines.append(f"{prefix}- **{k}:**")
                lines.append(render_value(v, indent + 1))
            else:
                lines.append(f"{prefix}- **{k}:** {v}")
        return "\n".join(lines)

    elif isinstance(value, list):
        lines = []
        for item in value:
            if isinstance(item, dict):
                # 处理带 key 的列表项
                if len(item) == 1:
                    key = list(item.keys())[0]
                    val = item[key]
                    lines.append(f"{prefix}- **{key}:**")
                    lines.append(render_value(val, indent + 1))
                else:
                    lines.append(render_value(item, indent))
            else:
                lines.append(f"{prefix}- {item}")
        return "\n".join(lines)

    else:
        return f"{prefix}{value}"


def render_skill(skill_path: pathlib.Path) -> str:
    """渲染 Skill 为 Markdown。"""
    with open(skill_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    lines = []
    lines.append(f"# {data.get('skill', 'Unknown Skill').title()}")
    lines.append("")
    lines.append(f"> **优先级:** {data.get('priority', 'N/A')}  ")
    lines.append(f"> **描述:** {data.get('description', '')}")
    lines.append("")

    # Activation
    if "activation" in data:
        lines.append("## 激活条件")
        lines.append(render_value(data["activation"]))
        lines.append("")

    # Principles
    if "principles" in data:
        lines.append("## 核心原则")
        lines.append(render_value(data["principles"]))
        lines.append("")

    # Constraints
    if "constraints" in data:
        lines.append("## 约束（禁止行为）")
        for c in data["constraints"]:
            lines.append(f"- ❌ {c}")
        lines.append("")

    # Exit Criteria
    if "exit_criteria" in data:
        lines.append("## 退出条件")
        for ec in data["exit_criteria"]:
            lines.append(f"- ✅ {ec}")
        lines.append("")

    # Methodology
    if "methodology" in data:
        lines.append("## 方法论")
        lines.append(render_value(data["methodology"]))
        lines.append("")

    # Orchestration
    if "orchestration" in data:
        lines.append("## 协同调度")
        lines.append(render_value(data["orchestration"]))
        lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("用法: python render-markdown.py <skill-file.yml>")
        print("示例: python render-markdown.py core-skills/bug-fix.yml")
        sys.exit(1)

    skill_path = pathlib.Path(sys.argv[1])
    if not skill_path.exists():
        print(f"❌ 文件不存在: {skill_path}")
        sys.exit(1)

    markdown = render_skill(skill_path)
    print(markdown)

    # 保存
    output_path = skill_path.with_suffix(".md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"\n💾 已保存到: {output_path}")


if __name__ == "__main__":
    main()
