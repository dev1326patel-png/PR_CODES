"""
File Operator - Personal Journal Manager
Author: [Your Name]
Date: [Current Date]
Description: Demonstrates file handling operations (read, write, append, delete),
             exception handling, and OOP principles including class design,
             encapsulation, and instance methods.
"""

import os
from datetime import datetime


class JournalManager:
    """Manages journal entries with file handling and exception handling."""

    def __init__(self, filename="journal.txt"):
        """
        Constructor initializes the journal file name.

        Args:
            filename (str): Name of the journal file. Defaults to 'journal.txt'.
        """
        self.filename = filename
        print(f"JournalManager initialized with file: {self.filename}")

    def add_entry(self):
        """
        Add a new journal entry to the file.
        Uses append mode ('a') to add entries without overwriting existing ones.
        Creates the file if it doesn't exist.
        """
        print("\n--- Add a New Entry ---")
        entry_text = input("Enter your journal entry:\n").strip()

        if not entry_text:
            print("Error: Entry cannot be empty. Please try again.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_entry = f"[{timestamp}]\n{entry_text}\n\n"

        try:
            # 'a' mode: append to file, create if not exists
            with open(self.filename, 'a', encoding='utf-8') as file:
                file.write(formatted_entry)
            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied. Cannot write to the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_entries(self):
        """
        Display all journal entries from the file.
        Uses read mode ('r') to read the file.
        Handles the case where the file does not exist.
        """
        print("\n--- View All Entries ---")

        try:
            # 'r' mode: read the file
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()

            if content.strip():
                print("\nYour Journal Entries:")
                print("=" * 50)
                print(content)
                print("=" * 50)
            else:
                print("No journal entries found. Start by adding a new entry!")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def search_entries(self):
        """
        Search for a specific keyword or date in the journal entries.
        Displays matching entries.
        """
        print("\n--- Search for an Entry ---")
        keyword = input("Enter a keyword or date to search: ").strip()

        if not keyword:
            print("Error: Search keyword cannot be empty.")
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()

            # Split entries by double newline (each entry separated by blank line)
            entries = [e.strip() for e in content.strip().split("\n\n") if e.strip()]

            matching_entries = [
                entry for entry in entries
                if keyword.lower() in entry.lower()
            ]

            if matching_entries:
                print("\nMatching Entries:")
                print("=" * 50)
                for entry in matching_entries:
                    print(entry)
                    print("-" * 50)
            else:
                print(f"\nNo entries were found for the keyword: {keyword}.")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def delete_entries(self):
        """
        Delete all journal entries by removing the file.
        Prompts user for confirmation before deleting.
        """
        print("\n--- Delete All Entries ---")

        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return

        confirm = input("Are you sure you want to delete all entries? (yes/no): ").strip().lower()

        if confirm == 'yes':
            try:
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            except PermissionError:
                print("Error: Permission denied. Cannot delete the file.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Deletion cancelled. Your entries are safe.")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("--- Personal Journal Manager ---")
    print("=" * 50)
    print("Please select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    print("=" * 50)


def main():
    """Main program loop."""
    print("=" * 60)
    print("Welcome to Personal Journal Manager!")
    print("=" * 60)
    print("This program demonstrates file handling, exception handling,")
    print("and OOP principles including class design and encapsulation.\n")

    journal = JournalManager("journal.txt")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            journal.add_entry()
        elif choice == '2':
            journal.view_entries()
        elif choice == '3':
            journal.search_entries()
        elif choice == '4':
            journal.delete_entries()
        elif choice == '5':
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option from the menu.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()