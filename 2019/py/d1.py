from util import get_things_from_file, DataTypes

D1_INPUT_FILE = "./d1_input_module_masses.txt"


def NegativeModuleMassException(Exception):
    pass


def calc_fuel_requirement(module_mass, fuel_accumulated):
    """
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


if __name__ == "__main__":
    print("Total fuel required: {}".format(d1_get_total_fuel_required()))
