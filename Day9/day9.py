#Level 1
age = int(input('Enter your age '))
while True:
    if (age >= 18) and (age < 80):
        print("You are old enough to drive")
        break
    elif age > 80:
        print("You are too old to drive")
        break
    elif (age < 18) and (age > 1):
        print("You need ",(18-age), " more years to learn to drive")
        break
    else:
        print("Enter your age again")
        age = int(input('Enter your age '))

#2  Comparing ages
my_age = 22
your_age = int(input("Enter your age "))
difference = my_age - your_age
if difference == 1:
    print("I am",difference,"year older than you")
elif difference > 1:
    print("I am",difference,"years older than you")
elif difference == 0: 
    print("We are agemates")
else:
    print("You are",abs(difference)," years older than me")
    
#3 input comparison
input1 = int(input("Enter a value: ")) 
input2 = int(input("Enter a value: "))
if input1 > input2:
    print(input1,'is greater than',input2)
elif input2 > input1:
    print(input2,'is greater than',input1)
else:
    print(input1,"is equal to",input2)
    
    
##Level 2
#1
grade = int(input("Enter your grade "))
if grade >= 80 and grade <= 100:
    print("Scored an A")
elif grade > 69 and grade < 80:
    print("Scored a B")
elif grade > 59 and grade < 70:
    print("Scored an C")
elif grade > 49 and grade < 60:
    print("Scored an D")
elif grade >=0 and grade < 50:
    print("You scored an F")

#2 seasons
month = input("Enter the current month ")
month = month.upper()

if month == "SEPTEMBER" or month == "OCTOBER" or month == "November":
    print("The season is Autumn")
elif month == "DECEMBER" or month == "JANUARY" or month == "FEBRUARY":
    print("The season is Winter")
elif month == "MARCH" or month == "APRIL" or month == "MAY":
    print("The season is Spring")
elif month == "JULY" or month == "AUGUST" or month == "JUNE":
    print("The season is Summer")    
    
# appending values in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
user_input = input("Enter a fruit: ")
if user_input in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(user_input)
    print(fruits)
    
#Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person.keys():
    print(person['skills'][(len(person['skills']))//2])
    if 'Python' in person['skills']:
        print("Yes there is python")
    else:
        print("Python does not exist")
else:
    print("Key does not exist")

if ['JavaScript', 'React'] == person['skills']:
    print('He is a front end developer')
elif ['Node', 'Python', 'MongoDB'] == person['skills']:
    print('He is a backend developer')
elif ['Node', 'React', 'MongoDB'] == person['skills']:
    print('He is a fullstack developer developer')

else:
    print('unknown title') 
    
if person['is_marred'] and person['country'] == "Finland":
    print(person['first_name'],person['last_name'],'lives in',person['country']+'.','He is married')
else:
    print("He is a ghost")