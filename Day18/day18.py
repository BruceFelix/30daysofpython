# Regular expressions
import re

# 1 Extract values and return their differences
# points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
# sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 -(-4) # 12
# first_value = re.findall('^-4', points)
# last_value = re.findall('8&', points)
# print(int(last_value) - int(first_value))

#2 valid python variable
def is_valid_variable(text):
    pattern = r"A-Za-z"
    result = re.findall(pattern, text)
    print(result)
is_valid_variable("Hello")