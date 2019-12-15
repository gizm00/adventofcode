import pytest

from day4 import is_password

@pytest.mark.parametrize("input, expected", [
(111111, False), # before part 2 modifications this was true
(223450, False),
(123789, False),
(112233, True),
(123444, False),
(111122, True)
])
def test_is_password(input, expected):
    assert is_password(input) == expected
