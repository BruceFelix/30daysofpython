"""File handling"""

import json
#Exercises: Level 1
#1 counts the number of lines and words in the 4 speeches
def words_lines_numbers(file):
    number_of_words = 0
    number_of_lines = 0
    with open(file) as speeches:
        num_lines = speeches.readlines()

        for lines in num_lines:
            number_of_lines += len(lines.split('.'))

        print(f'There are {number_of_lines} lines in {file}')

        for line in num_lines:
            number_of_words += len(line.split())

        print(f'There are {number_of_words} of words in {file}')
words_lines_numbers('obama_speech.txt')
words_lines_numbers('michelle_obama_speech.txt')
words_lines_numbers('donald_speech.txt')
words_lines_numbers('melina_trump_speech.txt')


#2 most spoken languages
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)
def ten_most_spoken_words(file, number):
    with open(file) as speakers:
        all_languages = speakers.readlines()
        languages = json.loads(all_languages)
        print(languages)
