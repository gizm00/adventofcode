from enum import Enum


class DataTypes(Enum):
    NUM = 0
    STRING = 1


def get_things_from_file(file_name, type):
    """
    Problems tend to have an input file that
    lists test data. This function returns a list
    of the desired type by processing each line 
    in the provided file_name
    """
    with open(file_name) as f:
        if type == DataTypes.NUM:
            return [int(num.strip()) for num in f.readlines() if num.strip() != ""]
