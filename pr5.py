"""
OOP Wrapper - Employee Management System
Author: [Your Name]
Date: [Current Date]
Description: Demonstrates OOP concepts including classes, inheritance,
             encapsulation, method overloading, method overriding,
             super(), and issubclass().
"""

# Global list to store all created objects
all_objects = []


class Person:
    """Base class representing a person."""

    def __init__(self, name="Unknown", age=0):
        """
        Constructor with default arguments (simulates method overloading).
        Can be called as Person() or Person(name) or Person(name, age).
        """
        self.name = name
        self.age = age
        print(f"Person created with name: {self.name} and age: {self.age}.")

    def display(self):
        """Display person details."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def __del__(self):
        """Destructor to clean up resources."""
        print(f"Person object for {self.name} has been deleted.")


class Employee(Person):
    """Derived class representing an employee. Inherits from Person."""

    def __init__(self, name="Unknown", age=0, employee_id="N/A", salary=0.0):
        """
        Constructor with default arguments (simulates method overloading).
        Calls parent constructor using super().
        """
        super().__init__(name, age)  # Call Person's constructor
        self.__employee_id = employee_id  # Private attribute (encapsulation)
        self.__salary = salary            # Private attribute (encapsulation)

    # Getter for employee_id
    def get_employee_id(self):
        return self.__employee_id

    # Setter for employee_id
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Error: Salary cannot be negative.")

    def display(self):
        """Override display() to include employee-specific details."""
        super().display()  # Call parent's display method
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary: ${self.__salary:.1f}")

    def __del__(self):
        """Destructor to clean up resources."""
        print(f"Employee object for {self.name} has been deleted.")
        super().__del__()


class Manager(Employee):
    """Derived class representing a manager. Inherits from Employee."""

    def __init__(self, name="Unknown", age=0, employee_id="N/A",
                 salary=0.0, department="General"):
        """
        Constructor with default arguments (simulates method overloading).
        Calls parent constructor using super().
        """
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        """Override display() to include department information."""
        super().display()  # Call Employee's display method
        print(f"Department: {self.department}")

    def __del__(self):
        """Destructor to clean up resources."""
        print(f"Manager object for {self.name} has been deleted.")
        super().__del__()


class Developer(Employee):
    """Derived class representing a developer. Inherits from Employee."""

    def __init__(self, name="Unknown", age=0, employee_id="N/A",
                 salary=0.0, programming_language="Python"):
        """
        Constructor with default arguments (simulates method overloading).
        Calls parent constructor using super().
        """
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        """Override display() to include programming language information."""
        super().display()  # Call Employee's display method
        print(f"Programming Language: {self.programming_language}")

    def __del__(self):
        """Destructor to clean up resources."""
        print(f"Developer object for {self.name} has been deleted.")
        super().__del__()


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("--- Python OOP Project: Employee Management System ---")
    print("=" * 50)
    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Demonstrate OOP Concepts")
    print("7. Exit")
    print("=" * 50)


def create_person():
    """Create a Person object."""
    print("\n--- Create a Person ---")
    name = input("Enter Name: ").strip()
    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid age. Defaulting to 0.")
        age = 0

    person = Person(name, age)
    all_objects.append(person)
    print(f"\nPerson created with name: {person.name} and age: {person.age}.")


def create_employee():
    """Create an Employee object."""
    print("\n--- Create an Employee ---")
    name = input("Enter Name: ").strip()
    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid age. Defaulting to 0.")
        age = 0
    employee_id = input("Enter Employee ID: ").strip()
    try:
        salary = float(input("Enter Salary: "))
    except ValueError:
        print("Invalid salary. Defaulting to 0.0.")
        salary = 0.0

    employee = Employee(name, age, employee_id, salary)
    all_objects.append(employee)
    print(f"\nEmployee created with name: {employee.name}, age: {employee.age}, "
          f"ID: {employee.get_employee_id()}, and salary: ${employee.get_salary():.1f}.")


def create_manager():
    """Create a Manager object."""
    print("\n--- Create a Manager ---")
    name = input("Enter Name: ").strip()
    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid age. Defaulting to 0.")
        age = 0
    employee_id = input("Enter Employee ID: ").strip()
    try:
        salary = float(input("Enter Salary: "))
    except ValueError:
        print("Invalid salary. Defaulting to 0.0.")
        salary = 0.0
    department = input("Enter Department: ").strip()

    manager = Manager(name, age, employee_id, salary, department)
    all_objects.append(manager)
    print(f"\nManager created with name: {manager.name}, age: {manager.age}, "
          f"ID: {manager.get_employee_id()}, salary: ${manager.get_salary():.1f}, "
          f"and department: {manager.department}.")


def create_developer():
    """Create a Developer object."""
    print("\n--- Create a Developer ---")
    name = input("Enter Name: ").strip()
    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid age. Defaulting to 0.")
        age = 0
    employee_id = input("Enter Employee ID: ").strip()
    try:
        salary = float(input("Enter Salary: "))
    except ValueError:
        print("Invalid salary. Defaulting to 0.0.")
        salary = 0.0
    programming_language = input("Enter Programming Language: ").strip()

    developer = Developer(name, age, employee_id, salary, programming_language)
    all_objects.append(developer)
    print(f"\nDeveloper created with name: {developer.name}, age: {developer.age}, "
          f"ID: {developer.get_employee_id()}, salary: ${developer.get_salary():.1f}, "
          f"and programming language: {developer.programming_language}.")


def show_details():
    """Display details of created objects."""
    print("\n--- Show Details ---")
    if not all_objects:
        print("No objects created yet.")
        return

    print("Choose details to show:")
    print("1. All Objects")
    print("2. Persons Only")
    print("3. Employees Only")
    print("4. Managers Only")
    print("5. Developers Only")

    choice = input("Enter your choice: ").strip()

    print("\n" + "-" * 40)
    if choice == '1':
        for obj in all_objects:
            print(f"\n[{type(obj).__name__} Details]")
            obj.display()
            print("-" * 40)
    elif choice == '2':
        persons = [obj for obj in all_objects if type(obj) == Person]
        if not persons:
            print("No Person objects found.")
        for obj in persons:
            print("\n[Person Details]")
            obj.display()
            print("-" * 40)
    elif choice == '3':
        employees = [obj for obj in all_objects if type(obj) == Employee]
        if not employees:
            print("No Employee objects found.")
        for obj in employees:
            print("\n[Employee Details]")
            obj.display()
            print("-" * 40)
    elif choice == '4':
        managers = [obj for obj in all_objects if type(obj) == Manager]
        if not managers:
            print("No Manager objects found.")
        for obj in managers:
            print("\n[Manager Details]")
            obj.display()
            print("-" * 40)
    elif choice == '5':
        developers = [obj for obj in all_objects if type(obj) == Developer]
        if not developers:
            print("No Developer objects found.")
        for obj in developers:
            print("\n[Developer Details]")
            obj.display()
            print("-" * 40)
    else:
        print("Invalid choice.")


def demonstrate_oop_concepts():
    """Demonstrate OOP concepts like issubclass() and encapsulation."""
    print("\n--- OOP Concepts Demonstration ---")

    # Demonstrate issubclass()
    print("\n1. issubclass() Checks:")
    print(f"   issubclass(Employee, Person)   -> {issubclass(Employee, Person)}")
    print(f"   issubclass(Manager, Employee)  -> {issubclass(Manager, Employee)}")
    print(f"   issubclass(Manager, Person)    -> {issubclass(Manager, Person)}")
    print(f"   issubclass(Developer, Employee)-> {issubclass(Developer, Employee)}")
    print(f"   issubclass(Person, Employee)   -> {issubclass(Person, Employee)}")

    # Demonstrate encapsulation
    print("\n2. Encapsulation Demonstration:")
    if all_objects:
        for obj in all_objects:
            if isinstance(obj, Employee):
                print(f"   Employee '{obj.name}' salary via getter: ${obj.get_salary():.1f}")
                obj.set_salary(obj.get_salary() + 5000)
                print(f"   After setter (+$5000): ${obj.get_salary():.1f}")
                break
        else:
            print("   No Employee objects found. Create one first.")
    else:
        print("   No objects found. Create some first.")

    # Demonstrate method resolution order
    print("\n3. Method Resolution Order (MRO):")
    print(f"   Manager MRO: {[cls.__name__ for cls in Manager.__mro__]}")
    print(f"   Developer MRO: {[cls.__name__ for cls in Developer.__mro__]}")

    # Demonstrate isinstance()
    print("\n4. isinstance() Checks:")
    if all_objects:
        for obj in all_objects[:3]:  # Show first 3 objects
            print(f"   {obj.name}: isinstance(obj, Person) = {isinstance(obj, Person)}")
    else:
        print("   No objects found. Create some first.")


def main():
    """Main program loop."""
    print("=" * 60)
    print("Welcome to the Employee Management System!")
    print("=" * 60)
    print("This program demonstrates OOP concepts: classes, inheritance,")
    print("encapsulation, method overloading, method overriding, super(),")
    print("and issubclass().\n")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            create_person()
        elif choice == '2':
            create_employee()
        elif choice == '3':
            create_manager()
        elif choice == '4':
            create_developer()
        elif choice == '5':
            show_details()
        elif choice == '6':
            demonstrate_oop_concepts()
        elif choice == '7':
            print("\nExiting the system. All resources have been freed.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        print("\n--- Choose another operation ---")


if __name__ == "__main__":
    main()