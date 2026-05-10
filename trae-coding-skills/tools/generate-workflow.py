#!/usr/bin/env python3
"""根据工作流模板生成复合 Prompt。"""

import yaml
import sys
import pathlib
from typing import Dict, List

SKILLS_DIR = pathlib.Path("core-skills")


def load_skill(skill_name: str) -> str:
    """加载指定 Skill 文件内容。"""
    # 尝试多种命名变体
    candidates = [
        f"{skill_name}.yml",
        f"{skill_name.replace('-', '_')}.yml",
        f"_{skill_name.lstrip('_')}.yml",
    ]

    for candidate in candidates:
        path = SKILLS_DIR / candidate
        if path.exists():
            return path.read_text(encoding="utf-8")

    # 模糊匹配
    for file in SKILLS_DIR.glob("*.yml"):
        if skill_name.replace("-", "") in file.stem.replace("-", "").replace("_", ""):
            return file.read_text(encoding="utf-8")

    return f"# [Warning] Skill '{skill_name}' not found\n"


def generate_workflow(workflow_path: pathlib.Path) -> str:
    """生成复合 Prompt。"""
    with open(workflow_path, "r", encoding="utf-8") as f:
        workflow = yaml.safe_load(f)

    output = []
    output.append("=" * 60)
    output.append(f"工作流: {workflow.get('workflow', 'Unknown')}")
    output.append(f"描述: {workflow.get('description', '')}")
    output.append("=" * 60)
    output.append("")

    # 加载 Orchestrator
    orchestrator = load_skill("orchestrator")
    output.append("【全局调度器】")
    output.append(orchestrator)
    output.append("\n" + "=" * 60 + "\n")

    # 加载各步骤 Skill
    steps = workflow.get("steps", {})
    for step_key, step_config in steps.items():
        output.append(f"【步骤 {step_key}】")
        output.append(f"目标: {step_config.get('output', 'N/A')}")
        output.append(f"退出条件: {step_config.get('exit_criteria', 'N/A')}")
        output.append("")

        skills = step_config.get("skills", [])
        for skill_name in skills:
            skill_content = load_skill(skill_name)
            output.append(f"--- Skill: {skill_name} ---")
            output.append(skill_content)
            output.append("")

        output.append("=" * 60)
        output.append("")

    # 约束
    constraints = workflow.get("constraints", [])
    if constraints:
        output.append("【工作流级约束】")
        for c in constraints:
            output.append(f"- {c}")
        output.append("")

    return "\n".join(output)


def main():
    if len(sys.argv) < 2:
        print("用法: python generate-workflow.py <workflow-file.yml>")
        print("示例: python generate-workflow.py workflow-templates/new-feature.yml")
        sys.exit(1)

    workflow_path = pathlib.Path(sys.argv[1])
    if not workflow_path.exists():
        print(f"❌ 文件不存在: {workflow_path}")
        sys.exit(1)

    result = generate_workflow(workflow_path)
    print(result)

    # 可选保存到文件
    output_path = workflow_path.with_suffix(".prompt.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"\n💾 已保存到: {output_path}")


if __name__ == "__main__":
    main()
