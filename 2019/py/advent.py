from copy import deepcopy
import logging
from util import get_things_from_file, DataTypes

INPUT_DIR = "../input_files/"
D1_INPUT_FILE = INPUT_DIR + "d1_input_module_masses.txt"
D2_INPUT_FILE = INPUT_DIR + "d2_input_opcodes.txt"
D3_INPUT_FILE = INPUT_DIR + "d3_input_wire_paths.txt"
logging.basicConfig(level = logging.DEBUG)

class NegativeModuleMassException(Exception):
    pass


class InvalidOpcodeException(Exception):
    pass
    
class TargetValuesNotFound(Exception):
    pass


def calc_fuel_requirement(module_mass, fuel_accumulated):
    """
    Day 1
    Given a mass, calculate the fuel required
    to propel the spacecraft
    :param: module_mass - integer mass of module
    Returns: integer fuel required
    """
    if module_mass < 0:
        raise NegativeModuleMassException(
            "Module mass is negative! {}".format(module_mass)
        )
    if module_mass == 0:
        return 0
    else:
        fuel_req = int(module_mass / 3) - 2

        # if the mass is so small the fuel required
        # is negative, return 0 fuel required
        # Note: the answer with the day 1 input was the
        # same regardless if this code was used or not
        # Oh LOL this is part 2 :D
        if fuel_req <= 0:
            return fuel_accumulated
        return calc_fuel_requirement(fuel_req, fuel_req + fuel_accumulated)


def d1_get_total_fuel_required():
    module_masses = get_things_from_file(D1_INPUT_FILE, DataTypes.NUM)
    return sum([calc_fuel_requirement(mass, 0) for mass in module_masses])


def d2_restore_state(program, pos1=12, pos2=2):
    """
    Restore the state to just before the computer
    caught fire.
    Modify the input program, which since python is pass
    by ref will modify the variable itself
    """
    program[1] = pos1
    program[2] = pos2


def d2_compute_program(program):
    """
    Run Intcode program
    :param program: list of integers comprising sets
    of the following format:
    position 0: opcode, one of util.Opcodes
    position 1: position of first operand for opcode
    position 2: position of second operand for opcode
    position 3: position at which to store operation result
    Once a command has been process, increment pointer by
    4 and execute the next instruction set
    Modify program in place. 
    """
    ptr = 0
    instruction_length = 4
    while ptr < len(program):
        op = program[ptr]
        if op == 1:
            program[program[ptr + 3]] = (
                program[program[ptr + 1]] + program[program[ptr + 2]]
            )
        elif op == 2:
            program[program[ptr + 3]] = (
                program[program[ptr + 1]] * program[program[ptr + 2]]
            )
        elif op == 99:
            return
        else:
            raise InvalidOpcodeException("Invalid opcode: {}".format(op))
        ptr = ptr + instruction_length

def d2_backcalculate_program_slow(program, target, min_value, max_value):
    """
    For Day 2 part 2, modify the source program by changing the values
    at addresses 1 and 2 to values [min_value:max_value] inclusive until address 0
    equals the target
    :param program: list of integers representing Intcode program
    :param target: integer target value for address 0 of the program
    :param min_value, max_value: the range of possible integers to replace
    at address 1 and 2
    Returns: the quantity 100*program[1]+program[2]
    """
    original_program = deepcopy(program)
    quantity = 0
    ptr = 0
    addr1_value = min_value
    addr2_value = min_value
    for addr1 in range(min_value, max_value+1):
        for addr2 in range(min_value, max_value+1):
            program_calc = deepcopy(original_program)
            d2_restore_state(program_calc, addr1, addr2)
            d2_compute_program(program_calc)
            if program_calc[0] == target:
                return 100 * program_calc[1] + program_calc[2]
    
    raise TargetValuesNotFound("Unable to find noun and verb :(")
            
def d3_find_wire_intersections(routes):
    """
    Return the grid location of wire intersections 
    :param routes: list of wire routes where each route is a 
    comma separated list of drawing directions
    i.e. a route R1,U2,L3 is right 1, up 2, left 3
    Returns: the circuit board and a list of intersection x,y tuples
    """
    
    # ugh wat
    intersections = set()
    all_routes = []
    origin = (0,0)
    for route in routes:
        pos_x = 0
        pos_y = 0
        mapped_route = set()
        for path in route.split(','):
            x_range_min = None
            x_range_max = None
            y_range_min = None
            y_range_max = None
            # for each step along a route, check if it is
            # in the circuit_board already. if so, add that
            # position to the intersections. If not, 
            # add that position to the circuit_board
            delta = int(path[1:])
            direction = path[0]
            if direction == 'L':
                x_range_max = pos_x - delta - 1
                x_range_min = pos_x
                incr = -1
                pos_x -= delta
            elif direction == 'R':
                x_range_min = pos_x
                x_range_max = pos_x + delta + 1
                incr = 1
                pos_x += delta
            elif direction == 'U':
                y_range_min = pos_y
                y_range_max = pos_y + delta + 1
                incr = 1
                pos_y += delta
            elif direction == 'D':
                y_range_min = pos_y
                y_range_max = pos_y - delta - 1
                incr = -1
                pos_y -= delta
            
            if x_range_min is not None:
                for i in range(x_range_min, x_range_max, incr):
                    pos = (i, pos_y)
                    match = [r for r in all_routes if pos in r]
                    if match:
                        logging.debug("adding intersection: {}".format(pos))
                        intersections.add(pos)
                    else:
                        mapped_route.add(pos)
            elif y_range_min is not None:
                for i in range(y_range_min, y_range_max, incr):
                    pos = (pos_x, i)
                    match = [r for r in all_routes if pos in r]
                    if match:
                        logging.debug("adding intersection: {}".format(pos))
                        intersections.add(pos)
                    else:
                        mapped_route.add(pos)
        
        all_routes.append(mapped_route)
    intersections.remove(origin)
    return all_routes, intersections
    
def d3_compute_closest_distance(intersections):
    """
    Find the shortest manhattan distance from the
    intersections to the origin (0,0)
    Keep in mind some tuples in the intersections list
    could be negative so take the abs when computing the distance
    :param intersections: list of (x,y) tuples
    """
    min_distance = None
    if len(intersections) == 0:
        print("no wire crossings found!")
        return 0
    else:
        for point in intersections:
            distance = abs(point[0]) + abs(point[1])
            if min_distance is None:
                min_distance = distance
            elif distance < min_distance:
                logging.debug("updating min_distance to {}".format(min_distance))
                min_distance = distance
        return min_distance
        
def d3_find_min_distance_wire_crossing(routes):
    board, intersections = d3_find_wire_intersections(routes)
    return d3_compute_closest_distance(intersections)

if __name__ == "__main__":
    # total_fuel_required = d1_get_total_fuel_required()))
    program = []
    with open(D3_INPUT_FILE) as f:
        program = f.readlines()
    #d2_restore_state(program)
    #d2_compute_program(program)
    #print("Value at position 0 of program result: {}".format(program[0]))
    #value = d2_backcalculate_program_slow(program, 19690720, 0, 99)
    #print("quantity for match: {}".format(value))
    print(d3_find_min_distance_wire_crossing(program))
