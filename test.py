# This script is written by thedonsclub


import random
import array as arr


def call_func(lent, sym, low, upr, numb):
    # numb = False
    # low = False
    # upr = False
    # sym = False

    global temp_pass_list, COMBINED_LIST, temp_pass
    MAX_LEN = lent

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')']

    if numb is True and upr is True:

        if low is True and sym is True:
            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

            rand_digit = random.choice(DIGITS)
            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)

            temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

        elif low is True and sym is False:
            # SYMBOLS = None
            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS

            rand_digit = random.choice(DIGITS)
            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            temp_pass = rand_digit + rand_upper + rand_lower

        elif low is False and sym is True:
            # LOCASE_CHARACTERS = None
            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + SYMBOLS

            rand_digit = random.choice(DIGITS)
            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)
            temp_pass = rand_digit + rand_upper + rand_symbol

        elif low is False and sym is False:
            # LOCASE_CHARACTERS = None
            # SYMBOLS = None

            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS

            rand_digit = random.choice(DIGITS)
            rand_upper = random.choice(UPCASE_CHARACTERS)
            temp_pass = rand_digit + rand_upper

    elif numb is True and upr is False:
        if low is True and sym is True:
            # UPCASE_CHARACTERS = None
            COMBINED_LIST = DIGITS + LOCASE_CHARACTERS + SYMBOLS

            rand_digit = random.choice(DIGITS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)
            temp_pass = rand_digit + rand_lower + rand_symbol

        elif low is True and sym is False:
            # SYMBOLS = None
            # UPCASE_CHARACTERS = None
            COMBINED_LIST = DIGITS + LOCASE_CHARACTERS

            rand_digit = random.choice(DIGITS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            temp_pass = rand_digit + rand_lower

        elif low is False and sym is True:
            # LOCASE_CHARACTERS = None
            # UPCASE_CHARACTERS = None
            COMBINED_LIST = DIGITS + SYMBOLS

            rand_digit = random.choice(DIGITS)
            rand_symbol = random.choice(SYMBOLS)
            temp_pass = rand_digit + rand_symbol

        elif low is False and sym is False:
            # LOCASE_CHARACTERS = None
            # SYMBOLS = None
            # UPCASE_CHARACTERS = None
            COMBINED_LIST = DIGITS

            rand_digit = random.choice(DIGITS)
            temp_pass = rand_digit
            # print('This type of password is Risky...')

    elif numb is False and upr is True:
        if low is True and sym is True:
            # DIGITS = None
            COMBINED_LIST = UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)
            temp_pass = rand_upper + rand_lower + rand_symbol

        elif low is True and sym is False:
            # SYMBOLS = None
            # DIGITS = None
            COMBINED_LIST = UPCASE_CHARACTERS + LOCASE_CHARACTERS

            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            temp_pass = rand_upper + rand_lower

        elif low is False and sym is True:
            # LOCASE_CHARACTERS = None
            # DIGITS = None
            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)
            temp_pass = rand_upper + rand_symbol

        elif low is False and sym is False:
            # LOCASE_CHARACTERS = None
            # SYMBOLS = None
            # DIGITS = None
            COMBINED_LIST = UPCASE_CHARACTERS

            rand_upper = random.choice(UPCASE_CHARACTERS)
            temp_pass = rand_upper

    elif numb is False and upr is False:
        if low is True and sym is True:
            # DIGITS = None
            # UPCASE_CHARACTERS = None
            COMBINED_LIST = LOCASE_CHARACTERS + SYMBOLS

            rand_lower = random.choice(LOCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)
            temp_pass = rand_lower + rand_symbol

        elif low is False and sym is True:
            # DIGITS = None
            # UPCASE_CHARACTERS = None
            # LOCASE_CHARACTERS = None
            COMBINED_LIST = SYMBOLS

            rand_symbol = random.choice(SYMBOLS)
            temp_pass = rand_symbol

        elif low is True and sym is False:
            # DIGITS = None
            # UPCASE_CHARACTERS = None
            # SYMBOLS = None
            COMBINED_LIST = LOCASE_CHARACTERS

            rand_lower = random.choice(LOCASE_CHARACTERS)

            temp_pass = rand_lower

        elif low is False and sym is False:
            # DIGITS = None
            # UPCASE_CHARACTERS = None
            # LOCASE_CHARACTERS = None
            # SYMBOLS = None

            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

            rand_digit = random.choice(DIGITS)
            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)

            temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(int(MAX_LEN) - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = arr.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x
    return password
