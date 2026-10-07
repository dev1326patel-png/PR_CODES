import datetime

name = input("enter your name :")
age = int(input("enter your age :"))
height = float(input("enter your height :"))
fav = int(input("enter your favorite number :"))

current_year = datetime.date.today().year
print(current_year)

birth_year = current_year - age 
print("your birth year is :",birth_year)

print(type(name))
print(id(name))
print(type(age))
print(id(age))
print(type(height))
print(id(height))
print(type(fav))
print(id(fav))


print("\n")
print("--"*10 + "your info" + "--"*10)
print(f"MY NAME IS {name}")
print(f"MY AGE IS {age}")
print(f"MY HEIGHT IS {height}")
print(f"MY FAVORITE NUMBER IS {fav}")
