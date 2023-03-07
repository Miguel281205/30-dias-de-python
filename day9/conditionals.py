age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")

else:
    print("Sorry mate, you have to be more than 18 to drive, when you reach that age you can drive a car, until then you should go on bus")

#    
your_age = int(input("Enter your age : "))
my_age  =17

if your_age == my_age:
    print("We both have the same age!")

elif your_age > my_age:
    print("You are older than me!")

elif your_age < my_age:
    print("You are younger than me!")

#
person1 = int(input("Enter a number : "))
person2 = int(input("Enter another number : "))

if person1 < person2:
    print("b is bigger")

elif person1 > person2:
    print("a is bigger")

elif person2 == person1:
    print("They are the same number")

#

mark = int(input("Type your mark: "))

if mark in range(0,49):
    print("Insuficiente")

elif mark in range(50,59):
    print("Suficiente")

elif mark in range(60,69):
    print("Bien")

elif mark in range(70,79):
    print("Notable")

elif mark in range(80,89):
    print("Notable alto")

elif mark in range(90,100):
    print("Sobresaliente")

#
month = input("Type a month: ")


if month in ["march", "april", "may"]:
    print("Spring")

elif month in ["june", "july", "august"]:
    print("Summer")

elif month in ["septiembre", "october", "november"]:
    print("Autumn")

elif month in ["december", "january", "february"]:
    print("Winter")

#

fruits = ["banana", "orange", "mango", "lemon"]

fruta = input("Type a fruit: ")

if fruta in fruits:
    print("Already exists in the list")
 
else:
    print("That does not appear in the list")
