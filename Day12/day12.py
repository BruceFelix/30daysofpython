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