# Functional Treat — Data Analyzer and Transformer

## Description
A menu-driven console program that analyses and transforms **1D and 2D lists**
while showcasing built-in functions, user-defined functions, `*args`,
`**kwargs`, `__doc__`, recursion, lambda functions, the `global` keyword,
multiple return values, and sorting with `sort()` vs `sorted()`.

## Features
- **Input Data** — manual 1D / 2D entry or two ready-made sample datasets.
- **Built-in Summary** — `len()`, `sum()`, `min()`, `max()`, `sorted()`.
- **Recursion** — factorial and Fibonacci, both implemented purely recursively.
- **Lambda Filter** — `filter(lambda x: …)` with ≥ / < threshold modes.
- **Lambda Map** — `map(lambda x: …)` to square, double, multiply, add, or stringify.
- **Sorting** — `list.sort()` (in-place, 1D) and `sorted()` (new list, 2D rows).
- **Multiple Returns** — `get_dataset_statistics()` returns `(min, max, sum, avg)`.
- **Advanced** — `*args` demo, `**kwargs` dataset-summary, duplicate & unique finders.
- **__doc__ Viewer** — prints every function's docstring from the menu.
- **2D Grid** — formatted display of a nested list.
- **Exit Option** — option 11 in the main menu.

## Project Structure
Functional-Treat/
│
├── functional_treat.py
├── README.md
└── sample_output.txt (optional)

## Assumptions
- Console-based; no third-party dependencies required.
- `DATASET` is a module-level global holding a 1D list or a 2D nested list.
- Numeric input is parsed as `int` when there is no `.`, otherwise `float`.
- Factorial is defined for `n >= 0`; Fibonacci is 0-indexed.
- Lambda filter option **1** = "≥ threshold"; option **2** = "< threshold".
- `sort()` mutates the global `DATASET` in place (1D). `sorted()` returns a new
  list of sorted rows for 2D data — the original `DATASET` is unchanged.
- Empty dataset => friendly "No data available" messages (no crash).

## How to Run
```bash
python functional_treat.py

## Concepts Demonstrated

| Concept | Where |
| --- | --- |
| Built-in functions | `display_data_summary()` |
| User-defined functions | `find_duplicates()`, `find_unique()`, `flatten_2d()`, … |
| `*args` | `show_args_demo(*args)` |
| `**kwargs` | `show_kwargs_demo(**kwargs)` |
| `__doc__` | `show_function_documentation()` |
| Recursion | `calculate_factorial()`, `calculate_fibonacci()` |
| Lambda | `filter(lambda …)`, `map(lambda …)` |
| `global` keyword | `update_global_summary()` |
| Multiple return values | `get_dataset_statistics()` |
| 1D / 2D lists | `input_data()`, `display_2d_grid()` |
| `sort()` vs `sorted()` | `sort_data()` |

## Author

[dev patel]