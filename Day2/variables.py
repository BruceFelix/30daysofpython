# Day 2: 30 Days of python programming
#Exercise Level1 
#### Declaring variables
first_name = "Jeff"
last_name = "Bezzos"
full_name = first_name + " "+ last_name
country = "USA"
city = "Washington DC"
age = 51
year = 2021
is_married = False
is_true = True
is_light_on = True
business, empire, skills_sets = "Enteprenuership", "Amazon", "Programmer"


#Exercises: Level 2
#1.1 Checking for data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(first_name))

#len() Built-in function
print(len(first_name))

#Comparing the lengths of names
if(len(first_name) > len(last_name)):
    print("first_name is longer")
else:
    print("last_name is longer")

# Arithmetics
num_one,num_two = 5,4
variable_total = num_one + num_two
variable_diff = num_one + num_two
variable_product = num_one * num_two
variable_division = num_one / num_two
variable_remainder = num_one % num_two
variable_exp = num_one ** num_two
variable_floor_division = num_one // num_two

# Circles
area_of_circle = 3.14 * 7 * 7
circum_of_circle = 3.14 * 7 * 2
##get input from user
radius = int(input("Enter a value to calculate the area: "))
area_of_circle = radius * 3.14 * radius
print(area_of_circle)

# Input(get user info)
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Which country are you from: ")
age = input("How old are you: ")

print(help('keywords'))