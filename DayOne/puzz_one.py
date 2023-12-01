import re

def main():
    """
    :rtype: Int representing the sum of each number built from each line (first and last digit)
            in puzzle1 (advent of code puzzle 1)
    """
    puzzle_one = open('../DayOne/puzzle1.txt', 'r', encoding='utf-8')
    lines = puzzle_one.read()
    calibration_values = []

    for line in lines.split("\n"):
        digits = re.sub(r'[^0-9]', '', line)

        if len(digits) == 1:
            new_value = digits + digits
            calibration_values.append(int(new_value))
            continue

        if len(digits) == 2:
            calibration_values.append(int(digits))
            continue

        if len(digits) > 2:
            new_value = digits[0] + digits[-1]
            calibration_values.append(int(new_value))

    print(sum(calibration_values))

    return 0

if __name__ == "__main__":
    main()
