# Exercises: Day 13
# 1 filter none negatives and zeros using comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [num for num in numbers if num > 0]
print(filtered)

#2 Flattening lists to 1D list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dimension = [number for rows in list_of_lists for row in rows for number in row]
print(one_dimension)

# 3 list comprehensions for tuples
list_of_tuples = [
    (i,
     i ** 0,
     i ** 1,
     i ** 2,
     i ** 3,
     i ** 4,
     i ** 5,
     )
     for i in range(11)
]
print(list_of_tuples)

#4 flattening a list of lists
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [[country,country[0:3],city]  for rows in countries for country,city in rows]
print(flattened_list)

#5 changing list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
city_country_dictionary = [{"country": country, "city": city} for rows in countries for country,city in rows]
print(city_country_dictionary)

#6 list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [first_name + " " +last_name for rows in names for first_name,last_name in rows]
print(concatenated_names)

#7 Lambda functions
slope_line = lambda x2,x1,y2,y1: (y2 - y1)/ (x2 - x1)
print(slope_line(10,8,16,4))