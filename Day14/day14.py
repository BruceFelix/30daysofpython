#High order functions
# Exercises: Level 1
# 1 Explain the following:
map = """
Executes a specified function for each item in an iterable
"""
filter = """
Returns an iterator where the items are filtered through a function to test if the item is accepted or not
"""
reduce = """
Gives an aggregate value oas an output
"""
"""They are all inbuilt functions."""


# 2 Difference betweeen higher order function, closure and decorator
Higher_order_fucntion = """
    A function is called a higher order function if it contains other functions as parameters
    or returns functions
"""
closure = """
    It is where by python allows a nested function to access the outer scope
    of the enclosing function.
"""
decorator = """
    A decorator is a design pattern in python that allows a user to add new
    functionality to an existing object without modifying its structure
"""
# 3 Call function before map, filter or reduce
# numbers = [1,2,3,4,5]
# def is_even(number):
#     if number % 2 == 0:
#         return True 
#     return False
# even_nums = filter(is_even, numbers )
# print(list(even_nums))

#4 Use for loop to print each country in the countries list.
#5 Use for to print each name in the names list.
#6 Use for to print each number in the numbers list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)
for name in names:
    print(name)
for number in numbers:
    print(number)

#Exercise: Level 2
# 1 Use map to create a new list by changing each country to uppercase in the countries list

def to_upper(country):
    return country.upper()
in_upper_country = map(to_upper, countries)
print(list(in_upper_country))

#2 Use map to create a new list by changing each number to its square in the numbers list

def to_square(num):
    return num ** 2
squared_nums = map(to_square, numbers)
print(list(squared_nums))

#3 Use map to change each name to uppercase in the names list
to_upper_names = map(to_upper, names)
print(to_upper_names)

#4 Use filter to filter out countries containing 'land'.
def countries_with_land(country):
    if "land" in country:
        return country
    return False
land_countries = filter(countries_with_land, countries)
print(list(land_countries))