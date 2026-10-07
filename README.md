# Python User Information Program

A simple beginner-level Python program that collects basic information from the user and displays it in a formatted way.

## About the Project

This project was created to practice fundamental Python concepts such as:

- User input
- Data type conversion
- Variables
- `if`/loop concepts
- Date and time using the `datetime` module
- String formatting
- `type()` function
- `id()` function
- Basic arithmetic operations

## Features

The program asks the user to enter:

- Name
- Age
- Height
- Favorite number

It then:

1. Gets the current year.
2. Calculates an approximate birth year from the entered age.
3. Displays the data type of each variable.
4. Displays the memory identity of each variable using `id()`.
5. Prints all the entered information in a formatted format.

## Technologies Used

- **Python 3**
- **datetime** — Python's built-in module for working with dates and times.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Open the project folder

```bash
cd your-repository-name
```

### 3. Run the Python program

```bash
python filename.py
```

Replace `filename.py` with the actual name of your Python file.

## Example

```text
Enter your name: Dev
Enter your age: 20
Enter your height: 5.5
Enter your favorite number: 7

2026
Your birth year is: 2006

<class 'str'>
<class 'int'>
<class 'float'>
<class 'int'>

--------------------your info--------------------
MY NAME IS Dev
MY AGE IS 20
MY HEIGHT IS 5.5
MY FAVORITE NUMBER IS 7
```

> **Note:** The calculated birth year is approximate because the program only uses the age and current year. It does not account for whether the user's birthday has already occurred this year.

## Learning Outcomes

Through this project, I practiced:

- Taking input using `input()`
- Converting strings using `int()` and `float()`
- Working with variables
- Performing arithmetic operations
- Using Python's `datetime` module
- Checking data types with `type()`
- Understanding object identity with `id()`
- Using f-strings for formatted output

## Future Improvements

Possible improvements include:

- Asking for the user's complete date of birth
- Calculating the exact age
- Adding input validation
- Creating a graphical user interface
- Saving user information to a file

## Author
Dev Patel

This project is part of my Python learning journey.
