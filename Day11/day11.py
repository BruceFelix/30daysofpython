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

#10 capitalization of words
def capitalize_list_items(a_list):
    new_list = []
    for word in a_list:
        new_list.append(word.title())
    print(new_list)

capitalize_list_items(["jeff", "bruce", "james", "charles"])

#11  adding items to list
crops = ["beans", "maize", "rice"]
def add_item(a_list, item):
    a_list.append(item)
    return a_list
print(add_item(crops, "wheat"))

#12 removing functions from a list
crops = ["beans", "maize", "rice", "wheat"]
def remove_item(a_list, item):
    a_list.remove(item)
    return a_list
print(remove_item(crops, "wheat"))

#13 sum of numbers
def sum_of_numbers(number):
    total = 0
    for i in range(1, number + 1,):
        total =total + i
    print(total)
sum_of_numbers(5)

# 14 sum of odds
def sum_of_odds(number):
    total = 0
    for i in range(1, number + 1):
        if i % 2 != 0:
            total = total + i
    print(total)
sum_of_odds(7)

#15 sum of even numbers in a range of number
def sum_of_even(number):
    total = 0
    for i in range(1, number + 1):
        if i % 2 == 0:
            total = total + i
    print(total)
sum_of_even(7) 

# Exercises: Level 2
# Function that returns the numbers of even and odd values in a number
def evens_and_odds(number):
    even =0
    odd = 0
    for i in range(number + 1):
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print("The number of odds are",odd)
    print("The number of evens are",even)
while True:
    number = int(input("Enter a positive number: "))
    if number >= 0:
        evens_and_odds(number)
        break
    else:
        continue

#2 factorial 
def factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    print(factorial)
factorial(10)

#3 checks if empty
def is_empty(para):
    if not para:
        print("Empty")
    else:
        print("Enter not empty")
para = input("Enter something: ")
is_empty(para)

#4 takes a list and calculates the following functions
#mean
def calculate_mean(a_list):
    total = 0
    for value in a_list:
        total =total + value
    average = total // len(a_list)
    print(average)
calculate_mean([1,2,3,4,5,6,7,8])
#median
items = [6, 1, 8, 2, 3]
def calculate_median(a_list):
    import statistics
    print(statistics.median(a_list))
calculate_median(items)

#range
def calculate_range(a_list):
    pass
#variance

# Exercises: Level 3
#1 prime numbers
def is_prime():
    number = int(input("Enter the input Range : "))
    for iter in range(1,number):
        for i in range(2,iter):
            if (iter%i==0):
                break
            else:
                print(iter)

#2 function to check if all items are unique in the list
# initializing list 
test_list = [1, 3, 4, 6, 7]
def unique_list(a_list):  
    print ("The original list is : " + str(a_list))
    flag = 0
    # using set() + len()
    # to check all unique list elements
    flag = len(set(a_list)) == len(a_list)
    # printing result
    if(flag) :
        print ("List contains all unique elements")
    else : 
        print ("List contains does not contains all unique elements")
  
unique_list(test_list)

#3 function to check if all the items are of the same data type
def all_same_data_types(a_list):
    for value in a_list:
        if isinstance(value) == str:
            print("The list is of type str")
        elif isinstance(value) == int:
            print("The list is of type str")
        elif isinstance(value) == dict:
            print("The list is of type str")
        elif isinstance(value) == float:
            print("The list is of type str")
        else:      
            print("The list is not unique")
all_same_data_types(['James', 1, 4.5, {"Name":"James"}])

# day