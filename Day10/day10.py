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
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
countries_with_land_in_their_name= []
for country in countries:
    if "land" in country:
        countries_with_land_in_their_name.append(country)  
print(countries_with_land_in_their_name)

#2 reverse the order using loop.
revesed = []
my_list = ['banana', 'orange', 'mango', 'lemon']
for fruit in my_list:
    revesed.insert(0,fruit)
print(revesed)

#3 level 3
# -->Go to the data folder and use the countries_data.py file.
#     >What are the total number of languages in the data
#     >Find the ten most spoken languages from the data
#     >Find the 10 most populated countries in the world