"""
Functional Treat - Data Analyzer and Transformer
================================================

A menu-driven console program that demonstrates:

    - Built-in functions  : len(), sum(), min(), max(), sorted()
    - User-defined funcs  : find_duplicates(), find_unique(), ...
    - *args and **kwargs  : show_args_demo(), show_kwargs_demo()
    - __doc__             : show_function_documentation()
    - Recursion           : calculate_factorial(), calculate_fibonacci()
    - Lambda functions    : filter() and map() with lambdas
    - global keyword      : DATASET_SUMMARY updated across functions
    - Multiple returns    : get_dataset_statistics()
    - 1D and 2D lists     : display_2d_grid()
    - sort() vs sorted()  : sort_data()

Author : [Your Name]
Date   : [Current Date]
"""

# --------------------------------------------------------------
# Global state
# --------------------------------------------------------------
DATASET = []            # Either a 1D list or a 2D nested list

DATASET_SUMMARY = {     # Global mutable summary
    "total_values": 0,
    "overall_mean": 0.0,
    "is_2d": False,
    "shape": None,
}


# ==============================================================
# Helper functions (used throughout)
# ==============================================================
def flatten_2d(data):
    """Flatten a 2D list (list of lists) into a single 1D list."""
    result = []
    for row in data:
        result.extend(row)
    return result


def get_flat_values():
    """Return a flat 1D list of all numeric values in the current DATASET."""
    if not DATASET:
        return []
    if DATASET_SUMMARY["is_2d"]:
        return flatten_2d(DATASET)
    return list(DATASET)


def update_global_summary():
    """Recompute and store the global DATASET_SUMMARY dictionary."""
    global DATASET_SUMMARY

    flat = get_flat_values()
    DATASET_SUMMARY["total_values"] = len(flat)
    DATASET_SUMMARY["overall_mean"] = (sum(flat) / len(flat)) if flat else 0.0
    DATASET_SUMMARY["is_2d"] = bool(DATASET and isinstance(DATASET[0], list))
    if DATASET_SUMMARY["is_2d"]:
        DATASET_SUMMARY["shape"] = (len(DATASET), len(DATASET[0]) if DATASET else 0)
    else:
        DATASET_SUMMARY["shape"] = (len(DATASET),) if DATASET else None


def _parse_number(token):
    """Convert a string token to int or float."""
    return float(token) if "." in token else int(token)


# ==============================================================
# 1. Input Data
# ==============================================================
def input_data():
    """Prompt the user to enter a 1D or 2D array manually, or load sample data."""
    global DATASET

    print("\n--- Input Data ---")
    print("1. Enter 1D array manually")
    print("2. Enter 2D array manually")
    print("3. Use sample 1D data")
    print("4. Use sample 2D data")
    print("5. Go Back")
    choice = input("Enter your choice: ").strip()

    try:
        if choice == "1":
            raw = input("Enter data for a 1D array (separated by spaces): ").strip()
            if not raw:
                print("Error: No data entered.")
                return
            DATASET = [_parse_number(x) for x in raw.split()]

        elif choice == "2":
            rows = int(input("Enter number of rows: ").strip())
            cols = int(input("Enter number of columns: ").strip())
            if rows <= 0 or cols <= 0:
                print("Error: Rows and columns must be positive.")
                return
            raw = input(f"Enter {rows * cols} values separated by spaces: ").strip()
            values = [_parse_number(x) for x in raw.split()]
            if len(values) != rows * cols:
                print(f"Error: Expected {rows * cols} values, got {len(values)}.")
                return
            DATASET = [values[i * cols:(i + 1) * cols] for i in range(rows)]

        elif choice == "3":
            DATASET = [34, 12, 56, 78, 43, 21, 90]
            print("Sample 1D data loaded:", DATASET)

        elif choice == "4":
            DATASET = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            print("Sample 2D data loaded.")
            display_2d_grid()

        elif choice == "5":
            return
        else:
            print("Invalid choice.")
            return

        update_global_summary()
        print("Data has been stored successfully!")

    except ValueError:
        print("Error: Please enter valid numeric values.")


def display_2d_grid():
    """Display the current 2D DATASET as a formatted grid."""
    if not DATASET or not DATASET_SUMMARY["is_2d"]:
        print("No 2D data available.")
        return
    print("\n2D Grid:")
    for row in DATASET:
        print("  " + " | ".join(f"{v:>6}" for v in row))


# ==============================================================
# 2. Display Data Summary (Built-in Functions)
# ==============================================================
def display_data_summary():
    """Display basic statistics using built-in functions len(), sum(), min(), max()."""
    flat = get_flat_values()
    if not flat:
        print("No data available. Please input data first (option 1).")
        return

    print("\nData Summary (built-in functions):")
    print(f"  Total elements    : {len(flat)}")
    print(f"  Minimum value     : {min(flat)}")
    print(f"  Maximum value     : {max(flat)}")
    print(f"  Sum of all values : {sum(flat)}")
    print(f"  Average value     : {sum(flat) / len(flat):.2f}")
    print(f"  Sorted (preview)  : {sorted(flat)[:5]} ...")
    print(f"  Data type         : {'2D' if DATASET_SUMMARY['is_2d'] else '1D'}")
    if DATASET_SUMMARY["is_2d"]:
        print(f"  Shape             : {DATASET_SUMMARY['shape']}")


# ==============================================================
# 3. Recursion
# ==============================================================
def calculate_factorial(n):
    """Recursively calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * calculate_factorial(n - 1)


def calculate_fibonacci(n):
    """Recursively calculate the nth Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative indices.")
    if n in (0, 1):
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


def recursion_menu():
    """Menu for recursive calculations."""
    print("\n--- Recursion Demonstration ---")
    print("1. Factorial")
    print("2. Fibonacci")
    print("3. Go Back")
    choice = input("Enter your choice: ").strip()

    try:
        if choice == "1":
            n = int(input("Enter a number to calculate its factorial: ").strip())
            if n > 20:
                print("Warning: factorials beyond 20! are huge; recursion may take a while.")
            print(f"Factorial of {n} is: {calculate_factorial(n)}")
        elif choice == "2":
            n = int(input("Enter the index n for Fibonacci: ").strip())
            print(f"Fibonacci({n}) = {calculate_fibonacci(n)}")
        elif choice == "3":
            return
        else:
            print("Invalid choice.")
    except ValueError as exc:
        print(f"Error: {exc}")


# ==============================================================
# 4. Lambda + filter()
# ==============================================================
def filter_data_by_threshold():
    """Filter data using a lambda function and the built-in filter()."""
    flat = get_flat_values()
    if not flat:
        print("No data available. Please input data first (option 1).")
        return

    try:
        raw = input("Enter a threshold value to filter data: ").strip()
        threshold = _parse_number(raw)

        print("\nFilter mode:")
        print("1. Values >= threshold")
        print("2. Values <  threshold")
        mode = input("Enter your choice: ").strip()

        if mode == "1":
            filtered = list(filter(lambda x: x >= threshold, flat))
            label = f"values >= {threshold}"
        elif mode == "2":
            filtered = list(filter(lambda x: x < threshold, flat))
            label = f"values < {threshold}"
        else:
            print("Invalid choice.")
            return

        if filtered:
            print(f"\nFiltered Data ({label}):")
            print(", ".join(map(str, filtered)))
        else:
            print(f"No values matched ({label}).")

    except ValueError:
        print("Error: Please enter a valid number.")


# ==============================================================
# 5. Lambda + map()
# ==============================================================
def transform_data_with_map():
    """Transform data using a lambda function and the built-in map()."""
    flat = get_flat_values()
    if not flat:
        print("No data available. Please input data first (option 1).")
        return

    print("\n--- Transform Data (Lambda + map) ---")
    print("1. Square each value")
    print("2. Double each value")
    print("3. Multiply by a custom factor")
    print("4. Add a custom constant")
    print("5. Convert all values to strings")
    choice = input("Enter your choice: ").strip()

    try:
        if choice == "1":
            mapped = list(map(lambda x: x ** 2, flat))
            label = "squared"
        elif choice == "2":
            mapped = list(map(lambda x: x * 2, flat))
            label = "doubled"
        elif choice == "3":
            factor = _parse_number(input("Enter the multiplier: ").strip())
            mapped = list(map(lambda x: x * factor, flat))
            label = f"multiplied by {factor}"
        elif choice == "4":
            constant = _parse_number(input("Enter the constant: ").strip())
            mapped = list(map(lambda x: x + constant, flat))
            label = f"added {constant}"
        elif choice == "5":
            mapped = list(map(lambda x: str(x), flat))
            label = "converted to strings"
        else:
            print("Invalid choice.")
            return

        preview = mapped[:20]
        tail = " ..." if len(mapped) > 20 else ""
        print(f"\nTransformed Data ({label}):")
        print(preview, tail)

    except ValueError:
        print("Error: Please enter valid numeric input.")


# ==============================================================
# 6. Sorting (sort() vs sorted())
# ==============================================================
def sort_data():
    """Sort 1D data in-place with list.sort(); sort 2D rows with sorted()."""
    if not DATASET:
        print("No data available. Please input data first (option 1).")
        return

    print("\n--- Sort Data ---")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter your choice: ").strip()

    if choice not in ("1", "2"):
        print("Invalid choice.")
        return
    ascending = (choice == "1")

    if DATASET_SUMMARY["is_2d"]:
        # sorted() returns a NEW list of rows; original DATASET untouched
        sorted_rows = [sorted(row, reverse=not ascending) for row in DATASET]
        print(f"\n2D Rows sorted in "
              f"{'Ascending' if ascending else 'Descending'} order (sorted()):")
        for row in sorted_rows:
            print("  ", row)
        print("\n(Note: list.sort() modifies in place; sorted() returns a new list. "
              "The original 2D DATASET is unchanged here.)")
    else:
        # list.sort() sorts the global DATASET in place
        DATASET.sort(reverse=not ascending)
        update_global_summary()
        print(f"\n1D Data sorted in "
              f"{'Ascending' if ascending else 'Descending'} order (list.sort() in-place):")
        print("  ", DATASET)


# ==============================================================
# 7. Statistics (Return Multiple Values)
# ==============================================================
def get_dataset_statistics():
    """Return multiple statistics about the dataset as a tuple (min, max, sum, avg)."""
    flat = get_flat_values()
    if not flat:
        return None
    total = sum(flat)
    average = total / len(flat)
    return min(flat), max(flat), total, average


def display_statistics():
    """Unpack and display the tuple returned by get_dataset_statistics()."""
    stats = get_dataset_statistics()
    if stats is None:
        print("No data available. Please input data first (option 1).")
        return

    min_val, max_val, total, avg = stats
    print("\nDataset Statistics (multiple return values):")
    print(f"  Minimum value     : {min_val}")
    print(f"  Maximum value     : {max_val}")
    print(f"  Sum of all values : {total}")
    print(f"  Average value     : {avg:.2f}")


# ==============================================================
# 8. Advanced (*args, **kwargs, duplicates, unique)
# ==============================================================
def show_args_demo(*args):
    """Accept multiple positional arguments with *args and display them."""
    print("\n--- *args Demonstration ---")
    print(f"Number of arguments received: {len(args)}")
    for i, arg in enumerate(args, 1):
        print(f"  Argument {i}: {arg!r}")
    numeric = [a for a in args if isinstance(a, (int, float))]
    if numeric:
        print(f"Sum of numeric arguments: {sum(numeric)}")


def show_kwargs_demo(**kwargs):
    """Accept keyword arguments with **kwargs and print a key-value summary."""
    print("\n--- **kwargs Demonstration ---")
    if not kwargs:
        print("No keyword arguments provided.")
        return
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


def find_duplicates(values):
    """User-defined: return a sorted list of values that appear more than once."""
    seen = set()
    duplicates = set()
    for v in values:
        if v in seen:
            duplicates.add(v)
        seen.add(v)
    return sorted(duplicates)


def find_unique(values):
    """User-defined: return a sorted list of the unique values."""
    return sorted(set(values))


def advanced_menu():
    """Sub-menu for advanced functional features."""
    while True:
        print("\n--- Advanced Operations ---")
        print("1. Demonstrate *args")
        print("2. Demonstrate **kwargs (Dataset Summary)")
        print("3. Find duplicates")
        print("4. Find unique values")
        print("5. Show function documentation (__doc__)")
        print("6. Go Back")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_args_demo(10, 20, 30, "hello", 3.14, True)

        elif choice == "2":
            show_kwargs_demo(
                total_values=DATASET_SUMMARY["total_values"],
                overall_mean=f"{DATASET_SUMMARY['overall_mean']:.2f}",
                is_2d=DATASET_SUMMARY["is_2d"],
                shape=DATASET_SUMMARY["shape"],
                data_source="User input / sample",
            )

        elif choice == "3":
            flat = get_flat_values()
            if not flat:
                print("No data available.")
            else:
                dups = find_duplicates(flat)
                print("Duplicates:", dups if dups else "None")

        elif choice == "4":
            flat = get_flat_values()
            if not flat:
                print("No data available.")
            else:
                print("Unique values:", find_unique(flat))

        elif choice == "5":
            show_function_documentation()

        elif choice == "6":
            break
        else:
            print("Invalid choice.")


# ==============================================================
# 9. Function Documentation via __doc__
# ==============================================================
def show_function_documentation():
    """Print the __doc__ of every key function in this program."""
    print("\n--- Function Documentation (__doc__) ---")
    functions = [
        input_data, display_data_summary, calculate_factorial,
        calculate_fibonacci, filter_data_by_threshold,
        transform_data_with_map, sort_data, get_dataset_statistics,
        show_args_demo, show_kwargs_demo, find_duplicates,
        find_unique, display_2d_grid,
    ]
    for func in functions:
        doc = (func.__doc__ or "No documentation.").strip()
        print(f"\n{func.__name__}():")
        for line in doc.splitlines():
            print(f"  {line}")


# ==============================================================
# Main menu and driver
# ==============================================================
def display_main_menu():
    """Display the main menu options."""
    print("\n" + "=" * 58)
    print("   Welcome to the Data Analyzer and Transformer Program")
    print("=" * 58)
    print("Main Menu:")
    print(" 1.  Input Data")
    print(" 2.  Display Data Summary (Built-in Functions)")
    print(" 3.  Calculate Factorial / Fibonacci (Recursion)")
    print(" 4.  Filter Data by Threshold (Lambda + filter)")
    print(" 5.  Transform Data (Lambda + map)")
    print(" 6.  Sort Data")
    print(" 7.  Display Dataset Statistics (Return Multiple Values)")
    print(" 8.  Advanced Operations (*args, **kwargs, duplicates, unique)")
    print(" 9.  Show Function Documentation (__doc__)")
    print("10.  Display 2D Grid (if 2D)")
    print("11.  Exit Program")
    print("=" * 58)


def main():
    """Main program loop."""
    print("Welcome to the Data Analyzer and Transformer Program")

    while True:
        display_main_menu()
        choice = input("Please enter your choice: ").strip()

        if choice == "1":
            input_data()
        elif choice == "2":
            display_data_summary()
        elif choice == "3":
            recursion_menu()
        elif choice == "4":
            filter_data_by_threshold()
        elif choice == "5":
            transform_data_with_map()
        elif choice == "6":
            sort_data()
        elif choice == "7":
            display_statistics()
        elif choice == "8":
            advanced_menu()
        elif choice == "9":
            show_function_documentation()
        elif choice == "10":
            display_2d_grid()
        elif choice == "11":
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()