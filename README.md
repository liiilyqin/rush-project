# Python Rush Project

This project contains five terminal-based ASCII art assignments implemented in Python.

Each assignment generates a different square or rectangle pattern based on the given width (`x`) and height (`y`).

---

## Project Structure

    RUSH-PROJECT/
    ├── rush-1-1/
    │   ├── rush.py
    │   └── main.py
    ├── rush-1-2/
    │   ├── rush.py
    │   └── main.py
    ├── rush-1-3/
    │   ├── rush.py
    │   └── main.py
    ├── rush-1-4/
    │   ├── rush.py
    │   └── main.py
    └── rush-1-5/
        ├── rush.py
        └── main.py

- `rush.py` contains the implementation of the `rush(x, y)` function.
- `main.py` is an optional local testing file.

---

## Requirements

- Python 3.x
- Terminal / command-line environment

---

## Usage

Example:

    cd rush-1-1
    python main.py

Example function call:

    from rush import rush

    rush(5, 3)

---

## Error Handling

If the provided width or height is invalid (`<= 0`), the program prints:

    Invalid size

to `stderr`.

---

## Notes

- All assignments are terminal-based.
- Output is generated using only the `print()` function.
- Edge cases such as `x == 1` or `y == 1` are handled according to the specification.
- Each assignment follows the required directory structure provided in the instructions.