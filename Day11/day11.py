#Level1
#1
def add_two_numbers(num1,num2):
    return num1 + num2
print(add_two_numbers(2,3))


#2
def area_of_circle(radius):
    pi = 22/7
    area = pi * radius * radius
    return area
print(area_of_circle(7))

#3summation of arbitrary number of arguments 
def add_all_nums(*nums):
    total = 0
    for num in nums:
        # if type()
        num = int(num)
        if isinstance(num, int) or isinstance(num, int):
            total += num 
        else:
            print("Some are not numbers")
    return total
print(add_all_nums(8,90,100,23)) #will come back

#4 degrees to Farenhites 
def convert_celcius_to_fahrenheit(degrees):
    faharenheit = (degrees * 9/5) + 32
    print(degrees,"°C is =",faharenheit,"°F")
print(convert_celcius_to_fahrenheit(100))

#5 function that checks  for seasons
def check_season(month):
    if month == "SEPTEMBER" or month == "OCTOBER" or month == "November":
        return "The season is Autumn"
    elif month == "DECEMBER" or month == "JANUARY" or month == "FEBRUARY":
        return "The season is Winter"
    elif month == "MARCH" or month == "APRIL" or month == "MAY":
        return "The season is Spring"
    elif month == "JULY" or month == "AUGUST" or month == "JUNE":
        return"The season is Summer" 
    else:
        return "That is not a month"
month_entered = input("Enter the current month ").upper() #converts the month to capital letters
print(check_season(month_entered))

#6 Calculates the slope of a linear equation
def calculate_slope(y2,y1,x2,x1):
    return (y2 -y1)/ (x2-x1)
print(calculate_slope(10,2,2,1))

#7 calculate the a quadratic equation
import math
def solve_quadratic_eqn( a, b, c): 
  
    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
      
    # checking condition for discriminant
    if dis > 0: 
        print(" real and different roots ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif dis == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 
      
    # when discriminant is less than 0
    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 
  
# Driver Program 
a = 1
b = 10
c = -24
  
# If a is 0, then incorrect equation
if a == 0: 
        print("Input correct quadratic equation") 
  
else:
    solve_quadratic_eqn(a, b, c)


# 8 Prints out values in a list 
def print_list(a_list):
    for value in a_list:
        print(value)
print_list([23,"jefe",12.1])

#9 reversing a list
def reverse_list(list1):
    for i in range(len(list1) - 1, -1, -1): 
        print(list1[i])
print(reverse_list([1,2,3,4,5,6,7,8]))

# capitalization of words
def capitalize_list_items(a_list):
    for word in list:
        word = word[0].upper() + word[1:]
    print(a_list)

capitalize_list_items(["Jeff", "Bruce"])
