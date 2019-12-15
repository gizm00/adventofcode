
INPUT_MIN = 123257
INPUT_MAX = 647015


def is_password(input):
    """
    Given an input number, identify if the number is
    a password.
    A password meets all of the following:
    * Is a 6 digit number
    * Within the min,max range provided
    * Has two adjacent digits that are the same
    * Digits never decrease from left to right
    Returns: True if input meets the above criteria, False if not
    """
    str_input = str(input)
    has_adjacent_digits = False
    digits_same_or_increase_l_r = True
    for i in range(len(str_input)-1):
        # are there any adjacent digits that are the same?
        if str_input[i] == str_input[i+1]:
            has_adjacent_digits = True

        # are there any adjacent digits that arent >= l to r?
        if int(str_input[i]) > int(str_input[i+1]):
            digits_same_or_increase_l_r = False

    return has_adjacent_digits and digits_same_or_increase_l_r


if __name__ == '__main__':
    passwords = []
    for i in range(INPUT_MIN,INPUT_MAX+1):
        if is_password(i):
            passwords.append(i)
    print("found {} passwords".format(len(passwords)))
