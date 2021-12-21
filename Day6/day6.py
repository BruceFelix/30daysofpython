#level1
#creating an empty tuple
empty_tuple = tuple()

# siblings tuple
sisters = ('Mitchell', 'Peshi', 'Nissy')
brothers = ('Alfred', 'Jude', 'Sammy')

#Joining siblings tuples
siblings = sisters + brothers

#total siblings
len_siblings = len(siblings)

#modify the siblings tuple and add your parents to it
family_members = list(siblings)
family_members.append("Dad") 
family_members.append('Mum')
family_members = tuple(family_members)

#level2
#unpacking the tuple
sister1_name,sister2_name,sister3_name,brother1_name,brother_name,brother3_name, *parents = family_members 

#create fruits,vegetables,animal products then join them.
fruits=('Apple','Mellon','Pawpaw')
vegatables = ('Kales','Spinach','Tomato')
animal_products = ('milk','meat', 'sausage')
food_stuff_tp = fruits + vegatables + animal_products

#change the food_stuff_tp to a list
list_food_stuff_tp = list(food_stuff_tp)

#slice out the middle item
print(list_food_stuff_tp[(len(list_food_stuff_tp))//2])

#slice out the last 3 and first 3 values
print(list_food_stuff_tp[0:3])
print(list_food_stuff_tp[-3:-1])

#delete the food_staff_tp completely
del list_food_stuff_tp
#checking if the list exists 
print(list_food_stuff_tp)

#Checking if an item exists in tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)