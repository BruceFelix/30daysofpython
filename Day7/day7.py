# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#level1
print(len(it_companies))
it_companies.add("Twitter")
it_Companies = {'Oracle', 'LinkedIn'}
it_companies.update(it_Companies)
print(it_Companies)
it_companies.remove('LinkedIn')
#Difference between remove and discard
"""We can remove an item from a set using remove() method. 
If the item is not found remove() method will raise errors, so it is good
to check if the item exist in the given set. However, discard() method doesn't raise any errors."""


#Level 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del it_companies
del A
del B


#level3
age_set = set(age)
print(len(age) < len(age_set))
sentence = "I am a teacher and I love to inspire and teach people"
list_sentence = sentence.split()
set_sentence = set(list_sentence)
print(set_sentence)