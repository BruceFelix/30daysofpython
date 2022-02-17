""""Exception Handling"""
# Exercise: Day 17
# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 
# 'Estonia','Russia']. Unpack the first five countries and store 
# them in a variable nordic_countries, store Estonia and Russia in es,
#  and ru respectively.

*nordic_countries, Estonia, Russia = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
print(nordic_countries,Estonia,Russia)