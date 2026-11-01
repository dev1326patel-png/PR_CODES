"""
Logic Box - Pattern Generator and Number Analyzer
Author: [Your Name]
Date: [Current Date]
Description: Demonstrates control structures, loops, range(), break/continue/pass,
             and nested loops for pattern generation.
"""

def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    print("=" * 50)

def pattern_generator():
    """Generate a right-angled triangle pattern using nested loops."""
    print("\n--- Pattern Generator ---")
    try:
        rows = int(input("Enter the number of rows for the pattern: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return

    # Validate row count
    if rows <= 0:
        print("Error: Number of rows must be a positive integer.")
        print("Returning to main menu.")
        return  # acts like a break out of this feature

    print("\nPattern:")
    # Nested loops: outer for rows, inner for columns
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()  # move to next line

    # Example of pass: placeholder for future pattern logic
    if rows > 10:
        pass  # TODO: add support for larger patterns later

def number_analyzer():
    """Analyze a range of numbers: odd/even and sum."""
    print("\n--- Number Analyzer ---")
    while True:
        try:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
        except ValueError:
            print("Invalid input! Please enter whole numbers.")
            continue

        if start > end:
            print("Error: End must be greater than or equal to start. Please try again.")
            continue
        else:
            break

    total_sum = 0
    print()
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"Number {num} is Even")
        else:
            print(f"Number {num} is Odd")
        total_sum += num

        # Example of continue: skip a specific number (e.g., skip 13)
        if num == 13:
            print("  (Skipping 13 as a demonstration of continue)")
            continue
        # Example of pass: placeholder for future analysis
        if num == 0:
            pass  # future logic for zero

    print(f"\nSum of all numbers from {start} to {end} is: {total_sum}")

def main():
    """Main program loop with menu-driven interface."""
    print("=" * 60)
    print("Welcome to the Pattern Generator and Number Analyzer!")
    print("=" * 60)
    print("This program can generate a right-angled triangle pattern")
    print("and analyze a range of numbers (odd/even and sum).")

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            pattern_generator()
        elif choice == '2':
            number_analyzer()
        elif choice == '3':
            print("\nExiting the program. Goodbye!")
            print("Thank you for using the Pattern Generator and Number Analyzer.")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()