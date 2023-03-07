#'Day 2: 30 Days of python program
from cProfile import run
from operator import truediv

first_name_var="Miguel"
last_name_var="Luna"
full_name_var="Miguel Luna"
country_var="ESPAÑA"
city_var="Jerez"
age_var="16"
year_var="2022"
is_married=False 
is_true=True
is_light_on=True
print(country_var , city_var)

print(type(full_name_var))
print(len(full_name_var))
print(len(last_name_var))

num_one=5
num_two=4

total=num_one+num_two
print(total)

diff=num_two-num_one
print(diff)

multiply=num_one*num_two
print(multiply)

divide=num_one/num_two
print(divide)

r=30
pi=3,14
diametro=30*2
areaofcircle=pi*r
circunferenciacirculo=pi*diametro

print(areaofcircle,circunferenciacirculo)

run 
help("keywords")