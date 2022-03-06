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

#5 Use filter to filter out countries having exactly six characters.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def six_letters(country):
    if len(country) == 6:
        return True
    return False
six_letter_countries = filter(six_letters, countries)
print(list(six_letter_countries))

#6 Use filter to filter out countries containing six letters and more in the country list.
def greater_than_six(country):
    if len(country) >= 6:
        return True
    return False
countries_greater_than_six = filter(greater_than_six, countries) 
print(list(countries_greater_than_six))

#7 Use filter to filter out countries starting with an 'E'
def starts_with_E(country):
    if country.startswith('E'):
        return True
    return False
countries_start_with_E = filter(starts_with_E, countries)
print(list(countries_start_with_E))

#8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
def is_even(num):
    if num % 2 == 0:
        return True
    return True
def total(num):
    total = 0
    total += num
    return total
mix_numbers = [0,12,3,223,34,23,234,5,456,56,34]
print(mix_numbers.map(to_square).filter(is_even).reduce(total))
# Didn't understand the question

#9 Declare a function called get_string_lists which takes a list as a parameter and then returns
#  a list containing only string items.
def get_string_lists(a_list):
    new_list = []
    for value in a_list:
        if isinstance(value, str):
            new_list.append(value)
    return new_list
mixed_list = [1, "Jeff", 23.3, "Bruce", "james"]
print(get_string_lists(mixed_list))

#10 Use reduce to sum all the numbers in the numbers list.
from functools import reduce
def reduce_sum(x, y):
    return x + y
result_sum = reduce(reduce_sum, numbers)
print(result_sum)

#11Use reduce to concatenate all the countries and to produce
#this sentence: Estonia, Finland, Sweden, Denmark, Norway, and
#Iceland are north European countries 
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
european = lambda x,y : f"{x}, {y}"
print(reduce(european,countries),"are North European countries")


#12 Declare a function called categorize_countries that returns a list of 
#countries with some common pattern (you can find the countries list in this
#repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from Day10 import countries

countries_land = []
countries_ia = []
countries_island = []
countries_stan = []
def categorize_countries():
    for country in countries.countries:
        if 'land' in country:
            countries_land.append(country)
        elif 'ia' in country:
            countries_ia.append(country)
        elif 'island' in country:
            countries_island.append(country)
        elif 'stan' in country:
            countries_stan.append(country)
    print(f"Countries with 'land' are: {countries_land}")
    print(f"Countries with 'ia' are: {countries_ia}")
    print(f"Countries with 'island' are: {countries_island}")
    print(f"Countries with 'stan' are: {countries_stan}")

categorize_countries()

#13Create a function returning a dictionary, where keys stand for starting letters 
#of countries and values are the number of country names starting with that letter.
my_dic = {}
def letter_values():
    for country in countries.countries:
        my_dic[country[0]] = my_dic.get(country[0],0) + 1
    print(my_dic)
letter_values()

#14 return the first ten countries in the list countries
def get_first_ten_countries(countries):
    return countries[0:10]
print(get_first_ten_countries(countries.countries))

#15 return the last 10 countries in the list countries
def get_last_ten_countries(countries):
    return countries[-11:-1: 1]
print(get_last_ten_countries(countries.countries))

#Exercises: Level 3
#1 Already done in the previous exercises