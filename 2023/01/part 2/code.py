import sys
import regex

digit_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
digit_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def first_and_last_digits(line):
    digits = regex.findall(
        '|'.join(digit_numbers + digit_names), # any digits or names
        line,
        overlapped=True # twone, eightwo, ...
    )
    first = digits[0]
    last = digits[-1]
    return (first, last)

def value_of_digits(digits):
    first, last = digits
    value = value_of_digit(first)*10 + value_of_digit(last)
    assert value >= 11
    assert value <= 99
    return value

def value_of_digit(digit):
    if digit in digit_names:
        value = digit_names.index(digit)+1
    else:
        value = digit_numbers.index(digit)+1
    assert value >= 1
    assert value <= 9
    return value

def line_value(line):
    line = line.strip()
    digits = first_and_last_digits(line)
    value = value_of_digits(digits)
    print(value, digits, line)
    return value

if __name__ == "__main__":
    total = 0
    for line in sys.stdin:
        total += line_value(line)
    print(total)
