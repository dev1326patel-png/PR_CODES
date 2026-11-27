# File Operator – Personal Journal Manager

## Description
A Python console application that demonstrates file handling operations and exception handling through a Personal Journal Manager. It uses OOP principles including class design, encapsulation, and instance methods.

## Features
- Add new journal entries with timestamps.
- View all journal entries from the file.
- Search for entries by keyword or date.
- Delete all entries with confirmation.
- Handle `FileNotFoundError`, `PermissionError`, and other exceptions gracefully.
- Menu-driven interface with input validation.

## Assumptions
- Journal entries are stored in `journal.txt` in the current directory.
- Each entry is prefixed with a timestamp in `[YYYY-MM-DD HH:MM:SS]` format.
- Entries are separated by a blank line.
- Search is case-insensitive and matches both timestamp and entry text.
- Data persists between program runs.

## File Handling Modes Used
| Mode | Operation | Method |
|------|-----------|--------|
| `'a'` | Append entries | `add_entry()` |
| `'r'` | Read entries | `view_entries()`, `search_entries()` |
| `os.remove()` | Delete file | `delete_entries()` |

## Class Structure
JournalManager
├── __init__(filename)
├── add_entry()
├── view_entries()
├── search_entries()
└── delete_entries()

## How to Run
1. Ensure Python 3.x is installed.
2. Clone the repository.
3. Run: `python personal_journal_manager.py`

## Sample Output
(Include the sample output from above)

## Author
[Your Name]
