
import logging

INPUT_MIN = 123257
INPUT_MAX = 647015
logging.basicConfig(level = logging.ERROR)

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
    digit_count = {}
    for i in range(len(str_input)-1):
        # are there any adjacent digits that are the same?
        if str_input[i] in digit_count.keys():
            digit_count[str_input[i]] += 1
        else:
            digit_count[str_input[i]] = 1
        if str_input[i] == str_input[i+1]:
            has_adjacent_digits = True

        # are there any adjacent digits that arent >= l to r?
        if int(str_input[i]) > int(str_input[i+1]):
            digits_same_or_increase_l_r = False

    logging.debug("Digit counts: {}".format(digit_count))

    # if we havent met the rules return false before bothering
    # to calculate the greater than 2 repeating rule for part 2
    if not(has_adjacent_digits and digits_same_or_increase_l_r):
        return False

    # because loop stops at -2 need to check the last digit
    # for repeating rule
    if str_input[-1] in digit_count.keys():
        digit_count[str_input[-1]] += 1

    # For part 2, we need to check if the adjacent digits
    # have > 2 counts. If so they are disqualified
    just_two = [d for d in digit_count.keys() if digit_count[d] == 2]
    if len(just_two) > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    passwords = []
    for i in range(INPUT_MIN,INPUT_MAX+1):
        if is_password(i):
            passwords.append(i)
    print("found {} passwords".format(len(passwords)))
