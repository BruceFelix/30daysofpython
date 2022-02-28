# Concatenate
# 1.
concatinating = ['Thirty', 'Days', 'Of', 'Python']
result = " ".join(concatinating)
print(result)

#2.
joining = ['Coding', 'For', 'All']
res = " ".join(joining)
print(res)

#3 
company = "Coding For All"
print(company) #4
print(len(company)) #5
print(company.upper()) #6
print(company.lower()) #7
print(company.capitalize()) #8
print(company.title()) #8 
print(company.swapcase()) #8
print(company[7:14]) #9 
print(company.find("Coding")) #10
print(company.replace('Coding', 'Python')) # 11



company = "Python For Everyone"

print(company.replace('Everyone', 'All'))
company1 = "Coding For All"
print(company1.split())

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print(company1[0])
print(company1[-1])
print(company1[10])
acronym = company[0] + company[7] + company[11]
abrv = company1[0] + company1[7] + company1[11]
print(acronym)
print(abrv)

print(company1.index("C"))
print(company1.index("F"))
print(company1.rfind("l"))
challenge = 'You cannot end a sentence with because because because is a conjuction'
print(challenge.find('because'))#you can use find or index function
print(challenge.rindex('because'))#you can use rfind or rindex function
print(challenge.replace("because", ""))
print(company1.startswith("Coding"))
print(company1.endswith("Coding"))
print('   Coding For All      '.strip(" "))
print('30DaysOfPython'.isidentifier())
print('30DaysOfPython'.isidentifier())
print(" ".join(['Django', 'Flask', 'Bottle', 'Pyramid','Falcon']))
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\t\tAge\tCountry\tCity \nAsabeneh\t250\tFinland\tHelsinki")
radius = 10
pi = 3.14
area = pi * radius ** 2
print(f'radius = {radius}')
print(f'area = {pi} * radius ** 2')
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')


a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

