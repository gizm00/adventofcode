import pytest
from advent import *


def test_calc_fuel_requirement():
    assert calc_fuel_requirement(6, 0) == 0


def test_restore_state():
    program = [0, 1, 2, 3, 4, 5, 6]
    d2_restore_state(program)
    assert program[1] == 12 and program[2] == 2


@pytest.mark.parametrize(
    "program_in, program_out",
    [
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ],
)
def test_compute_program(program_in, program_out):
    d2_compute_program(program_in)
    assert program_in == program_out
