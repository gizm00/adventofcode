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


@pytest.mark.parametrize("routes, min_distance",
[
(["R8,U5,L5,D3","U7,R6,D4,L4"], 6),
(["R75,D30,R83,U83,L12,D49,R71,U7,L72",
"U62,R66,U55,R34,D71,R55,D58,R83"], 159),
(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
"U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"], 135)])
def test_find_wire_crossings(routes, min_distance):
    assert d3_find_min_distance_wire_crossing(routes) == min_distance

@pytest.mark.parametrize("routes, min_steps",
[
(["R8,U5,L5,D3","U7,R6,D4,L4"], 30),
(["R75,D30,R83,U83,L12,D49,R71,U7,L72",
"U62,R66,U55,R34,D71,R55,D58,R83"], 610),
(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
"U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"], 410)
])
def test_minimize_signal_delay(routes, min_steps):
    assert d3_minimize_signal_delay(routes)[1] == min_steps


def test_d3_compute_steps():
    board = OrderedDict()
    board[(0,1)] = None
    board[(1,0)] = None
    intersection = (1,0)
    assert d3_compute_steps(board, intersection) == 1
