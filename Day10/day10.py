#level 1
# 1 iterating from 0 to 10
count = 0
while count < 11:
    print(count)
    count +=1
    
#2 Iterating from 10 to 0 counting downwards
number = 10
while number > 0:
    print(number)
    number -= 1

#3 creating a right angled triangle
for i in range(8):# counts the number of rows
    for j in range(i): # uses the value of i to generate the hashes
        print("#", end='')# ends the hashes with spaces instead of newlines
    print()#breaks the line to a new line

#4 creating a rectangle using for loop
for i in range(0,8):
    for j in range(0,8):
        print("#",end='')
    print()

#5 Multiplication table from 0 to 10
for j in range (11):
    print(j,'x',j,"=",j*j )

#6 iterating over the list and printing out the values
for language in  ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(language)

#7 for loop to iterate over 0 to 100 printing even numbers only
for i in range(0,100,2):
    print(i)
    
#8 for loop to iterate over 0 to 100 printing odd numbers only
for i in range(0,100):
    if i % 2 != 0:
        print(i)
    
#level 2
#1 for loop to iterate from 0 to 100 and print the sum of all numbers
summation = 0
for i in range (0,101):
    summation = summation + i
print(summation)
    
#2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even = 0
odd = 0
for i in range (0,101):
    if i % 2 == 0:
        even +=i
    else:
        odd += i
print(even)
print(odd)

#Level3
#1Loop through the countries and extract all the countries containing the word land.
import countries 
countries_with_land_in_their_name= []
for country in countries.countries:
    if "land" in country:
        countries_with_land_in_their_name.append(country)  
print(countries_with_land_in_their_name)

#2 reverse the order using loop.
reversed = []
my_list = ['banana', 'orange', 'mango', 'lemon']
for fruit in my_list:
    reversed.insert(0,fruit)
print(reversed)

#3 level 3
# -->Go to the data folder and use the countries_data.py file.
#     >What are the total number of languages in the data
#     >Find the ten most spoken languages from the data
#     >Find the 10 most populated countries in the world

import countries_data
# 1total number of languages in the world
total_languages = 0
languages =[]
for dic in countries_data.countries:
    # print(dic['languages'])
    total_languages += len(dic['languages'])
    languages += dic['languages']
print(len(set(languages)))
print(total_languages)

# 10 most spoken languages in the world\
result = {}
for language in languages:
    if languages.count(language) == 0:
        result.keys = language
        result.value = 1
    else:
        result.key = language
        result.values = languages.count(language)
print(result)