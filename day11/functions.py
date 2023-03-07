import math

def add_two_numbers(x,y):
    return x + y

#
def area_of_a_circle(r):
    return 3.1416 * r**2
    

#
def add_all_nums(N):
    for i in N:
        N = N + 1
        print(N)


#
def from_c_to_f(celsius):
    return(celsius * 9 / 5) + 32 

#
def check_season(month):
    if month in ["march", "april", "may"]:
        return("Spring")
    
    elif month in ["june", "july", "august"]:
        return("Summer")

    elif month in ["septiembre", "october", "november"]:
        return("Autumn")

    elif month in ["december", "january", "february"]:
        return("Winter")

#
def print_list(E):
    E = []
    for i in E:
        print(i)



  