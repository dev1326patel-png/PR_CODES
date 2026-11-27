# PR7: Multi-Utility Toolkit

## Project Overview
Multi-Utility Toolkit is a Python console application that demonstrates modular programming by combining Python standard-library modules, custom modules, and a custom package. It provides date/time tools, mathematical calculations, random data generation, UUID creation, dynamic module exploration, and text-file operations.

## Requirements
- Python 3.10 or newer
- No third-party packages are required

## Project Structure
```text
PR7/
├── main.py
├── PR7.py
├── toolkit_package/
│   ├── __init__.py
│   ├── file_operations.py
│   └── math_utilities.py
├── data/                 # Created automatically when file operations are used
└── README.md
```

## Concepts Demonstrated
- Built-in modules: `datetime`, `time`, `math`, `random`, `uuid`, `secrets`, and `string`
- Custom modules: `file_operations.py` and `math_utilities.py`
- Package organization using `toolkit_package/__init__.py`
- `if __name__ == "__main__"` entry-point pattern
- Dynamic module inspection with `dir()`
- Menu-driven loops, functions, exception handling, and input validation
- Text-file creation, writing, reading, and appending

## Main Menu
1. Date and Time Utilities
2. Mathematical Utilities
3. Random Utilities
4. UUID Generator
5. File Operations
6. Dynamic Module Exploration
7. Exit

## How to Run
Open a terminal in the `PR7` folder and run:
```bash
python main.py
```
Alternatively:
```bash
python PR7.py
```

## File Storage
Text files created by the application are stored in the `data/` folder. The folder is created automatically. File operations are restricted to filenames, and the application adds the `.txt` extension when it is missing.

## Assumptions and Notes
- The application is console-based.
- Python 3.10+ is installed.
- File operations are intended for UTF-8 text files.
- Stopwatch and countdown use the `time` module.
- Passwords and OTPs use the `secrets` module for secure random selection; general random examples use `random`.
- UUID identifiers are generated with `uuid.uuid4()`.
- Files persist between program runs because they are stored on disk.
- Invalid input and common file errors are handled without intentionally terminating the application.

## Testing Checklist
- [ ] Run the main menu and test invalid menu input.
- [ ] Check current date/time, date difference, and date formatting.
- [ ] Test stopwatch and a short countdown.
- [ ] Calculate factorial, compound interest, trigonometric values, and areas.
- [ ] Generate random numbers, passwords, OTPs, and samples.
- [ ] Generate multiple UUID4 identifiers.
- [ ] Create, write, read, append, and list text files.
- [ ] Open dynamic module exploration and return to the menu.
