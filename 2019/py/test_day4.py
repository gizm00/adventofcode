import pytest

from day4 import is_password

@pytest.mark.parametrize("input, expected", [
(111111, True),
(223450, False),
(123789, False)
])
def test_is_password(input, expected):
    assert is_password(input) == expected
