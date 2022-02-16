import random, string
#Exercises: Level 1
#1 Generates a random 6 figure digit as a user id
def random_user_id():
    digits = random.choices(string.digits, k=3)
    letters = random.choices(string.ascii_letters, k=3)
    return "".join(random.sample(digits + letters, 6))
print(random_user_id())

#2 generates users id according to the characters needed and number of ids needed
def user_id_gen_by_user():
    num_of_chars = int(input("Enter number of characters to generate: "))
    num_of_ids = int(input("Enter number of IDS you need: "))

    digits = random.choices(string.digits, k=100)
    letters = random.choices(string.ascii_letters, k=100)

    for ids in range(1, num_of_ids + 1):
        print(''.join(random.sample(digits + letters, num_of_chars )))
user_id_gen_by_user()

#3 Generates rgb colors
def rgb_color_gen():
    val1 = random.randint(0, 255)
    val2 = random.randint(0, 255)
    val3 = random.randint(0, 255)
    return "rgb({},{},{})".format(val1,val2,val3)
print(rgb_color_gen())


#Exercises: Level 2
# 1 generating hexadecimal colors
def list_of_hexa_colors(numb_of_colors):
    colors = []
    letters = random.choices("ABCDEF", k=6)
    digits = random.choices("1234567890", k = 6)
    for color in range(1, numb_of_colors + 1):
        color =  "#" + ''.join(random.sample(digits + letters, 6))
        colors.append(color)
    print(colors)

# 2 generating rgb colors
def list_of_rgb_colors(numb_of_colors):
    colors = []
    val1 = random.randint(0, 255)
    val2 = random.randint(0, 255)
    val3 = random.randint(0, 255)
    for color in range(1, numb_of_colors + 1):
        color = "rgb({},{},{})".format(val1,val2,val3)
        colors.append(color)
    print(colors)

# 3 hexa or rgb generator
def hex_or_rgb():
    type = input("Enter the color type you need: rgb or hexa: ")
    number = int(input("Enter the number of colors you need: "))
    if type.lower() == "hexa":
        list_of_hexa_colors(number)
    elif type.lower() == "rgb":
        list_of_rgb_colors(number)
    else:
        print("Invalid type of color")
hex_or_rgb()