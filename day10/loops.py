numbers = 1,2,3,4,5,6,7,8,9,10

for x in numbers:
    print(x)

count = 0
while count <= 10:
    print(count)
    count = count + 1

#
new_numbers = 10,9,8,7,6,5,4,3,2,1,0

for x in new_numbers:
    print(x)

count2 = 10
while count2 >= 0:
    print(count2)
    count2  = count2 - 1

#
hags = "#"

for i in range(1,9):
    i = i * hags
    print(i)

#
hags_2 = "#"

for i in range(1,9):
    for r in range(1,9):
        print(hags_2, end="")


#
for i in range(0,11):
    print(i, "x", i, "=", i*i)


#
list = ["Bryant", "Jordan", "O'neal", "James", "Curry"]

for contents in list:
    print(contents) 

#
for i in range(0,101):
    print(i)

#

for num in range(0,5005):
    num = num + 1
    print("All is ", num)

#
contries = ["Spain, France, Germany, Austria, Poland, UK, USA, Russia"]

for country in contries:
    if "pain" in country:
        print(country)
