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
        # if type(num) == 'int' or  type(num) == 'float':
        total += num 
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
month_entered = input("Enter the current month ")
month_entered = month_entered.upper()
print(check_season(month_entered))