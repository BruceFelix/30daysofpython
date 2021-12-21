#1 Creating an empty dictionary
dog = {} # or dog = dict()

#2 Adding values to the dog dictionary
dog['name'] = "xela"
dog['color'] = "Black"
dog['breed'] = 'German shephard'
dog['legs'] = 'Long spotted white'
dog['age'] = '12 dog years'
# print(dog)

#3 student dict
student = {
    'first_name' : "Bruce",
    'last_name' : 'Macharia',
    'gender' : 'Male',
    'age' : 22,
    'marrital status' : 'Single',
    'skills' : ['HTML','CSS', 'PYTHON', 'NETWORKING'],
    'Country' : 'Kenya',
    'City' : 'Nairobi',
    'Address' : {
        'streetcode' : 588,
        'code' : '01000'
    }
}
# print(student)

#4length of dict
print(len(student))

#5 type of data 
print(type(student['skills']))

#6 modify the skills values
student['skills'].append('Touch typing')
student['skills'].append('Little of js,java,php')
# print(student)

#7 get keys as list
print(student.keys())

#8 get values as list
print(student.values())

#9 changing dict to a list of tuples
print(student.items())

#10 deleting an item from the dic
del student['skills']

#11 deleting one of the dictionaries
del student['Address']

print(student)