#!/usr/bin/env python3
"""校验 Skill YAML 格式合规性。"""

import yaml
import sys
import pathlib
from typing import List, Dict, Any

REQUIRED_TOP_LEVEL = ["skill", "priority", "description", "activation", "principles"]
REQUIRED_ACTIVATION = ["trigger_on"]
VALID_PRIORITIES = ["highest", "high", "medium", "low"]


def validate_file(path: pathlib.Path) -> List[str]:
    """校验单个 YAML 文件。"""
    errors = []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [f"{path}: YAML 解析失败 - {e}"]
    except Exception as e:
        return [f"{path}: 读取失败 - {e}"]

    if data is None:
        return [f"{path}: 文件为空"]

    # 检查必填字段
    for field in REQUIRED_TOP_LEVEL:
        if field not in data:
            errors.append(f"{path}: 缺少必填字段 '{field}'")

    # 检查 priority 有效性
    priority = data.get("priority", "").lower()
    if priority and priority not in VALID_PRIORITIES:
        errors.append(f"{path}: priority '{priority}' 无效，应为 {VALID_PRIORITIES}")

    # 检查 activation 结构
    activation = data.get("activation", {})
    if not any(k in activation for k in REQUIRED_ACTIVATION):
        errors.append(f"{path}: activation 必须包含 trigger_on")

    # 检查 constraints 存在性（推荐）
    if "constraints" not in data:
        errors.append(f"{path}: 警告 - 缺少 constraints 字段（强烈推荐）")

    return errors


def validate_all(directory: pathlib.Path) -> Dict[str, List[str]]:
    """校验目录下所有 YAML 文件。"""
    all_errors = {}

    for pattern in ["*.yml", "*.yaml"]:
        for file_path in directory.rglob(pattern):
            # 跳过 examples 目录中的 YAML（可能不是 skill）
            if "examples" in str(file_path):
                continue
            errors = validate_file(file_path)
            if errors:
                all_errors[str(file_path.relative_to(directory))] = errors

    return all_errors


def main():
    target = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(".")

    if not target.exists():
        print(f"❌ 路径不存在: {target}")
        sys.exit(1)

    print(f"🔍 校验目录: {target.absolute()}\n")

    errors = validate_all(target)

    if not errors:
        print("✅ 所有 Skill YAML 格式合规！")
        sys.exit(0)

    print(f"❌ 发现 {len(errors)} 个文件存在问题：\n")
    for file_path, file_errors in errors.items():
        print(f"📄 {file_path}")
        for err in file_errors:
            print(f"   - {err}")
        print()

    sys.exit(1)


if __name__ == "__main__":
    main()
