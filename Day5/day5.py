#Exercise: Level 1
#1 
empty_list = []

#2
shoes_list = ['Jordan','Timberland', "clarks", 'Gucci','Loafers']

#3
print(len(shoes_list))

#4
print(shoes_list[0],shoes_list[2], shoes_list[-1])

#5
mixed_data_types = ['Bruce', "22", '177cm', 'single', '588-01000']

#6
it_companies = ['Facebook', 'Google', 'Microsoft','Apple', "IBM","Oracle", "Amazon"]

#7
print(it_companies)

#8
print("The number of IT companies: ",len(it_companies))

#9
print(it_companies[0],it_companies[3],it_companies[-1])

#10
it_companies[0] = "Huawei"
print(it_companies)

#11
it_companies.append("Facebook")
print(it_companies)

#12
it_companies.insert(4, "Pixer")
print(it_companies)

#13
it_companies[1] = it_companies[1].upper()
print(it_companies)

#14
print(("#").join(it_companies))

#15
print("Facebook" in it_companies)

#16 
it_companies.sort()
print(it_companies)

#17

it_companies.reverse()
print(it_companies)

#18
print(it_companies[0:3])

#19 
print(it_companies[-3:])

#20 
middle_company = it_companies[     ((len(it_companies))//2)     ]
print(middle_company)

#21
it_companies.pop(0)
print(it_companies)

#22
it_companies.pop(((len(it_companies))//2))

#23
it_companies.pop(-1)
print(it_companies)

#24
it_companies.clear()
print(it_companies)

#25
del it_companies

#26
front_end = ['HTML','CSS','JS','React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

combined_list = front_end + back_end

#27
full_stack = combined_list.copy()
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)
print(combined_list)

#Exercises: Level 2
#1
ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()
print('Sorted ages',ages)
min_value = min(ages)
max_value = max(ages)

# append max and min to ages
ages.append(min_value)
ages.append(max_value)
ages.sort()
print(ages)

#median
mid = len(ages)//2
median_value =  (ages[mid - 1] + ages[~mid])/2
print(median_value)

#average 
average = sum(ages)/ len(ages)
print(average)

#range 
# range_value = range(max_value,min_value)
range_value = max_value - min_value
print(range_value)

#absolute values 
print(abs(min_value - average)> abs(max_value - average))

#middle country
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
countries.sort()
middle_country = len(countries)//2
print(countries[middle_country])

#division of countries
first_half = countries[0:middle_country + 1]
other_half = countries[middle_country +1:]
print(len(first_half), len(other_half))

#unpacking values
countrys_list = ['China','Russia', 'USA','Finland','Norway','Denmark']
first_country,second_country ,third_country, *scandavian_countries = countrys_list
