import pytest
from d1 import calc_fuel_requirement


def test_calc_fuel_requirement():
    assert calc_fuel_requirement(6) == 0
