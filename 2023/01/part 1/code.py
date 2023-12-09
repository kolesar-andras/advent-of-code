import sys
import re

def first_and_last_digits(line):
    digits = re.findall(r"([0-9])", line)
    first = digits[0]
    last = digits[-1]
    return (first, last)

def value_of_digits(digits):
    first, last = digits
    value = int(first + last)
    return value

def line_value(line):
    line = line.strip()
    print(line)
    digits = first_and_last_digits(line)
    value = value_of_digits(digits)
    print(digits, value)
    return value

if __name__ == "__main__":
    total = 0
    for line in sys.stdin:
        total += line_value(line)
    print(total)
