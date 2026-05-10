# ✅ 测试文件（先写测试，再写实现）

import pytest
from example import validate_password


class TestValidatePassword:
    """密码强度校验器测试。"""

    def test_valid_password(self):
        is_valid, errors = validate_password("HelloWorld1")
        assert is_valid is True
        assert errors == []

    def test_too_short(self):
        is_valid, errors = validate_password("Hi1A")
        assert is_valid is False
        assert "密码长度必须至少 8 位" in errors

    def test_missing_uppercase(self):
        is_valid, errors = validate_password("helloworld1")
        assert is_valid is False
        assert "必须包含至少一个大写字母" in errors

    def test_missing_lowercase(self):
        is_valid, errors = validate_password("HELLOWORLD1")
        assert is_valid is False
        assert "必须包含至少一个小写字母" in errors

    def test_missing_digit(self):
        is_valid, errors = validate_password("HelloWorld")
        assert is_valid is False
        assert "必须包含至少一个数字" in errors

    def test_multiple_errors(self):
        is_valid, errors = validate_password("hi")
        assert is_valid is False
        assert len(errors) == 3  # 长度、大写、数字

    def test_empty_password(self):
        is_valid, errors = validate_password("")
        assert is_valid is False
        assert len(errors) >= 3

    def test_exactly_eight_chars_valid(self):
        """边界：刚好 8 位且满足所有条件。"""
        is_valid, errors = validate_password("Abcdef1!")
        assert is_valid is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
