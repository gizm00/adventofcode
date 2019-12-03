from copy import deepcopy
from util import get_things_from_file, DataTypes

INPUT_DIR = "../input_files/"
D1_INPUT_FILE = INPUT_DIR + "d1_input_module_masses.txt"
D2_INPUT_FILE = INPUT_DIR + "d2_input_opcodes.txt"


def NegativeModuleMassException(BaseException):
    pass


def InvalidOpcodeException(BaseException):
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
            


if __name__ == "__main__":
    # total_fuel_required = d1_get_total_fuel_required()))
    program = []
    with open(D2_INPUT_FILE) as f:
        program = [int(elem) for elem in f.readline().strip().split(",")]
    #d2_restore_state(program)
    #d2_compute_program(program)
    #print("Value at position 0 of program result: {}".format(program[0]))
    value = d2_backcalculate_program_slow(program, 19690720, 0, 99)
    print("quantity for match: {}".format(value))
