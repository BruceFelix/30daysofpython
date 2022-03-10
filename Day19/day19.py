"""File handling"""

import json
#Exercises: Level 1
#1 counts the number of lines and words in the 4 speeches
# def words_lines_numbers(file):
#     number_of_words = 0
#     number_of_lines = 0
#     with open(file) as speeches:
#         num_lines = speeches.readlines()# Reads the files line by line

#         print(f'There are {len(num_lines)} lines in {file}')

#         for line in num_lines:
#             number_of_words += len(line.split(" "))

#         print(f'There are {number_of_words} of words in {file}')
# words_lines_numbers('obama_speech.txt')
# words_lines_numbers('michelle_obama_speech.txt')
# words_lines_numbers('donald_speech.txt')
# words_lines_numbers('melina_trump_speech.txt')


#2 most spoken languages
# python dictionary
def ten_most_spoken_words():
    pass
# ten_most_spoken_words()
# with open('countries_data.json', 'r') as speakers:
#     languages = json.load(speakers)
#     print(languages)
with open("countries_data.json", 'r') as speakers:
    languages = json.load(speakers)
    print(languages)
    