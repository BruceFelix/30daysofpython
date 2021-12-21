# my_age = 22
# my_height = 5.9
# a_complex_value = 3 + 5j

# #area of a triangle
# print("Working with triangles")
# print("The area of a triangle")
# print("______________________________________________________________")
# base = float(input("Enter base: "))
# height = float(input("Enter height: "))
# print("The area of the triangle is",0.5* base * height)
# print("______________________________________________________________")
# #perimeter of a triangle
# print("The perimeter of a triangle")
# print("______________________________________________________________")
# side_a = int(input("Enter side a: "))
# side_b = int(input("Enter side b: "))
# side_c = int(input("Enter side c: "))
# print("The perimeter of the triangle is",side_c + side_a + side_b)
# print("______________________________________________________________")


# #area and perimeter of a rectangle
# print("Working with rectanlge")
# ##variables prompt
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# ## area
# print()
# print("The area of a rectangles")
# area_of_a_rectangle = length * width
# print("The area of the rectangle with width",width,"and length",length,"is",area_of_a_rectangle)
# print("______________________________________________________________")

# ## Perimeter
# print("The perimeter of a rectangle")
# perimeter_of_a_rectangle = 2 * (length + width)
# print("The perimeter of the rectangle with width",width,"and length",length,"is",perimeter_of_a_rectangle)
# print("______________________________________________________________")


# #area and circumfrence of a circle
# print("Working with circles")
# print("______________________________________________________________")
# ##variables prompt
# radius = float(input("Enter the radius: "))
# pi = 3.14
# ## area
# print("The area of a circles")
# area_of_a_circle = pi * radius * radius
# print("The area of the circle with radius",radius,"is",area_of_a_circle)
# print("______________________________________________________________")
# #circumfrence of a circle
# print("The circumfrence of a circle")
# circumfrence_of_a_circle = 2 * pi * radius
# print("The circumfrence of the circle with radius",radius,"is",circumfrence_of_a_circle)
# print("______________________________________________________________")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# y intercept 
# y1, x2 = 0, 0
# x1 = (y1 + 2)/2 
# y2 = 2 * x2 -2
# m1 = (y2 - y1)/(x2 - x1)

# print("The x intercept is",x1,"The y intercept is",y2," the slope is",m1)

# #finding the slope
# x1, x2 = 2 ,6
# y1, y2 = 2, 10
# m = (y2 - y1)/(x2 - x1)
# print("The gradient is",m,"when given (2, 2),(6,10) ")
# # Compare the slopes in both tasks
# print(m1 == m)

# # Try to use different x values and figure out at what x value y is 0.
# x = -3
# print("Y =",x**2 + 6*x + 9, "when x = -3")
# #Comparing the lengths
# print(len("python")> len("Jargon"))


# The and and in keyword
# print("on" in "python" and "on" in "jargon")
# print("jargon" in "I hope this course is not full of jargon")
# print("on" not in "python" and "on" not in"jargon")

# #Python string
# python_length = len("python")
# python_length_to_float = float(python_length)
# python_length_to_string = str(python_length)

# #Even numbers
# number = int(input("Enter a value to check if it is divisible by 2: "))
# if number%2 == 0:
#     print("Even Number")
# else:
#     print( "Odd")

# print(7//3 == int(2.7))
# print('10' == 10)
# # print(int('9.8') == 10)/results in an error


# ## pay
# hours = int(input("Enter your hours: "))
# rate_per_hour = int(input("Enter the rate per hour: "))
# print("Weekly earning is ",hours* rate_per_hour)

# #age in seconds
# years = int(input("Enter your age: "))
# years *= 31556926
# print("You have lived for",years,"seconds.")


# script to print this
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
for i in range(1,6):
    print(i**1,i**0,i**1,i**2,i**3 )
        