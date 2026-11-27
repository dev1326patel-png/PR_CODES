"""PR7: Multi-Utility Toolkit - menu-driven Python console application."""

from datetime import datetime, date, timedelta
import math
import random
import secrets
import string
import time
import uuid

from toolkit_package import file_operations, math_utilities


def read_int(prompt: str, minimum: int | None = None) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if minimum is not None and value < minimum:
                print(f"Enter a value greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_float(prompt: str, minimum: float | None = None) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if not math.isfinite(value):
                print("Please enter a finite number.")
                continue
            if minimum is not None and value < minimum:
                print(f"Enter a value greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def pause() -> None:
    input("\nPress Enter to return to the main menu...")


def datetime_menu() -> None:
    while True:
        print("\n--- DATE & TIME UTILITIES ---")
        print("1. Show current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format a date")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("0. Back")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Current date/time:", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
        elif choice == "2":
            try:
                first = date.fromisoformat(input("First date (YYYY-MM-DD): ").strip())
                second = date.fromisoformat(input("Second date (YYYY-MM-DD): ").strip())
                delta = second - first
                print(f"Difference: {abs(delta.days)} day(s)")
            except ValueError:
                print("Invalid date. Use YYYY-MM-DD (for example, 2026-11-27).")
        elif choice == "3":
            try:
                value = datetime.strptime(
                    input("Enter date and time (YYYY-MM-DD HH:MM): ").strip(),
                    "%Y-%m-%d %H:%M"
                )
                print("Formatted:", value.strftime("%A, %d %B %Y at %I:%M %p"))
            except ValueError:
                print("Invalid format. Example: 2026-11-27 14:30")
        elif choice == "4":
            input("Press Enter to start the stopwatch...")
            start = time.perf_counter()
            input("Stopwatch running. Press Enter to stop...")
            print(f"Elapsed time: {time.perf_counter() - start:.2f} seconds")
        elif choice == "5":
            seconds = read_int("Countdown duration in seconds: ", 0)
            print("Countdown started.")
            try:
                while seconds:
                    print(f"Time remaining: {seconds} second(s)", end="\r", flush=True)
                    time.sleep(1)
                    seconds -= 1
                print("\nTime is up!")
            except KeyboardInterrupt:
                print("\nCountdown cancelled.")
        elif choice == "0":
            return
        else:
            print("Invalid menu choice. Select 0 to 5.")
        pause()


def math_menu() -> None:
    while True:
        print("\n--- MATHEMATICAL UTILITIES ---")
        print("1. Factorial")
        print("2. Compound interest")
        print("3. Trigonometry (degrees)")
        print("4. Area calculator")
        print("0. Back")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                number = read_int("Enter a non-negative integer: ", 0)
                print(f"{number}! = {math_utilities.factorial(number)}")
            elif choice == "2":
                principal = read_float("Principal amount: ", 0)
                rate = read_float("Annual interest rate (%): ", 0)
                years = read_float("Time in years: ", 0)
                frequency = read_int("Compounding periods per year: ", 1)
                amount, interest = math_utilities.compound_interest(
                    principal, rate, years, frequency
                )
                print(f"Final amount: {amount:.2f}")
                print(f"Compound interest: {interest:.2f}")
            elif choice == "3":
                angle = read_float("Angle in degrees: ")
                for name, value in math_utilities.trigonometry(angle).items():
                    print(f"{name}(angle) = {value:.6f}")
            elif choice == "4":
                print("1. Circle  2. Rectangle  3. Triangle")
                shape = input("Choose shape: ").strip()
                if shape == "1":
                    area = math_utilities.circle_area(read_float("Radius: ", 0))
                elif shape == "2":
                    area = math_utilities.rectangle_area(
                        read_float("Length: ", 0), read_float("Width: ", 0)
                    )
                elif shape == "3":
                    area = math_utilities.triangle_area(
                        read_float("Base: ", 0), read_float("Height: ", 0)
                    )
                else:
                    print("Invalid shape.")
                    continue
                print(f"Area = {area:.4f}")
            elif choice == "0":
                return
            else:
                print("Invalid menu choice. Select 0 to 4.")
        except (ValueError, OverflowError) as error:
            print("Could not complete calculation:", error)
        pause()


def random_menu() -> None:
    while True:
        print("\n--- RANDOM UTILITIES ---")
        print("1. Generate random integer")
        print("2. Generate random list")
        print("3. Generate secure password")
        print("4. Generate OTP")
        print("5. Random sample from values")
        print("0. Back")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            low = read_int("Minimum: ")
            high = read_int("Maximum: ")
            if low > high:
                print("Minimum cannot be greater than maximum.")
            else:
                print("Random number:", random.randint(low, high))
        elif choice == "2":
            count = read_int("How many numbers? ", 1)
            low = read_int("Minimum value: ")
            high = read_int("Maximum value: ")
            if low > high:
                print("Minimum cannot be greater than maximum.")
            else:
                print("Random list:", [random.randint(low, high) for _ in range(count)])
        elif choice == "3":
            length = read_int("Password length (minimum 8): ", 8)
            alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_"
            password = "".join(secrets.choice(alphabet) for _ in range(length))
            print("Generated password:", password)
        elif choice == "4":
            digits = read_int("OTP length (4-10): ", 4)
            if digits > 10:
                print("OTP length cannot exceed 10.")
            else:
                print("Generated OTP:", "".join(secrets.choice(string.digits) for _ in range(digits)))
        elif choice == "5":
            values = [item.strip() for item in input("Enter comma-separated values: ").split(",") if item.strip()]
            if not values:
                print("Please enter at least one value.")
            else:
                count = read_int(f"Number of items to select (1-{len(values)}): ", 1)
                if count > len(values):
                    print("Sample size cannot exceed the number of available values.")
                else:
                    print("Random sample:", random.sample(values, count))
        elif choice == "0":
            return
        else:
            print("Invalid menu choice. Select 0 to 5.")
        pause()


def uuid_menu() -> None:
    print("\n--- UUID UTILITIES ---")
    count = read_int("How many UUID4 identifiers should be generated? ", 1)
    for index in range(1, count + 1):
        print(f"{index}. {uuid.uuid4()}")
    pause()


def file_menu() -> None:
    while True:
        print("\n--- TEXT FILE OPERATIONS ---")
        print("1. Create file")
        print("2. Write/overwrite file")
        print("3. Read file")
        print("4. Append to file")
        print("5. List saved text files")
        print("0. Back")
        choice = input("Choose an option: ").strip()
        try:
            if choice in {"1", "2", "3", "4"}:
                filename = input("Filename (example: notes.txt): ").strip()
                if choice == "1":
                    path = file_operations.create_file(filename)
                    print(f"Created: {path.name}")
                elif choice == "2":
                    content = input("Enter content: ")
                    path = file_operations.write_file(filename, content)
                    print(f"Written to: {path.name}")
                elif choice == "3":
                    print("\n--- FILE CONTENT ---")
                    print(file_operations.read_file(filename))
                    print("--- END ---")
                else:
                    content = input("Enter content to append: ")
                    path = file_operations.append_file(filename, content)
                    print(f"Appended to: {path.name}")
            elif choice == "5":
                names = file_operations.list_files()
                print("Saved files:", ", ".join(names) if names else "No text files found.")
            elif choice == "0":
                return
            else:
                print("Invalid menu choice. Select 0 to 5.")
        except (OSError, ValueError) as error:
            print("File operation failed:", error)
        pause()


def explore_modules() -> None:
    print("\n--- DYNAMIC MODULE EXPLORATION ---")
    for module in (datetime, time, math, random, uuid, file_operations, math_utilities):
        print(f"\n{module.__name__}")
        public_names = [name for name in dir(module) if not name.startswith("_")]
        print(", ".join(public_names[:30]))
    print("\nThe dir() function lists the available names/attributes in a module.")
    pause()


def main() -> None:
    while True:
        print("\n" + "=" * 48)
        print("          PR7: MULTI-UTILITY TOOLKIT")
        print("=" * 48)
        print("1. Date and Time Utilities")
        print("2. Mathematical Utilities")
        print("3. Random Utilities")
        print("4. UUID Generator")
        print("5. File Operations")
        print("6. Dynamic Module Exploration")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_modules()
        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
