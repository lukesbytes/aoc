import aoc.common.input


def check_digit_prefix(line, char_allowed):
    """
    Check if line (string) prefix is a digital value.
    If allowed, digital value prefix is searched in text form.

    :param line:
    :param char_allowed:
    :return:
    """
    digit_s = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
               "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    if line[0].isdigit():
        return line[0]

    if char_allowed:
        try:
            first = next(digit_s[ds] for ds in digit_s.keys() if line.startswith(ds))[0]
            return first
        except StopIteration:
            pass

    return None


def get_first_and_last_digit(line, char_allowed):
    """
    Get first and last digits and combine into digital value
    :param line:
    :param char_allowed:
    :return:
    """
    first = ""
    last = ""

    for fi in range(len(line)):
        first = check_digit_prefix(line[fi:], char_allowed)
        if first is not None:
            break

    for li in range(len(line)-1, -1, -1):
        last = check_digit_prefix(line[li:], char_allowed)
        if last is not None:
            break

    return int(f"{first}{last}")


def get_calibration(data, char_allowed=False):
    """
    Reduce all calibration values to sum

    :param data:
    :param char_allowed:
    :return:
    """
    cs = 0
    for v in data:
        c = get_first_and_last_digit(v, char_allowed)
        cs += c
    return cs


# Read lines
data_input = aoc.common.input.read_input(year=2023, day=1, split='\n')

print(get_calibration(data_input))
print(get_calibration(data_input, char_allowed=True))
