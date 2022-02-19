"""File handling"""
#Exercises: Level 1
#1 counts the number of lines and words in the 4 speeches
with open('obama_speech.txt') as obama:
    lines = obama.readlines()
    print(lines)
    lines = lines.split('.')
    print(lines)

