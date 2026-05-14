import sys


def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    # Special case: single row or single column
    if x == 1 or y == 1:
        for _ in range(y):
            print("*" * x)
        return

    for row in range(y):
        line = ""

        for col in range(x):
            if row == 0 and col == 0:
                line += "/"
            elif row == 0 and col == x - 1:
                line += "\\"
            elif row == y - 1 and col == 0:
                line += "\\"
            elif row == y - 1 and col == x - 1:
                line += "/"
            elif row == 0 or row == y - 1 or col == 0 or col == x - 1:
                line += "*"
            else:
                line += " "

        print(line)