# ✅ 示例：测试驱动开发（Python）

"""
需求：实现一个密码强度校验器。
规则：
- 长度 >= 8
- 包含至少一个大写字母
- 包含至少一个小写字母
- 包含至少一个数字
- 返回 (is_valid: bool, errors: list[str])
"""

import re
from typing import Tuple, List


def validate_password(password: str) -> Tuple[bool, List[str]]:
    """校验密码强度。"""
    errors = []

    if len(password) < 8:
        errors.append("密码长度必须至少 8 位")

    if not re.search(r"[A-Z]", password):
        errors.append("必须包含至少一个大写字母")

    if not re.search(r"[a-z]", password):
        errors.append("必须包含至少一个小写字母")

    if not re.search(r"\d", password):
        errors.append("必须包含至少一个数字")

    return (len(errors) == 0, errors)
