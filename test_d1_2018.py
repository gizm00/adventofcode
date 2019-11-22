import pytest
from d1_2018 import find_repeat_frequency

@pytest.mark.parametrize("nums,expected", [
    ([+1, -1], 0),
    ([+3, +3, +4, -2, -4], 10),
    ([-6, +3, +8, +5, -6], 5),
    ([+7, +7, -2, -7, -4], 14)
])
def test_find_repeat(nums, expected):
    assert find_repeat_frequency(nums) == expected