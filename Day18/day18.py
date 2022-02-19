# Regular expressions
import re
#Exercise: Level 1 
# Most frequent word.
paragraph = """I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."""
def countWords(lines):
    wordDict = []
    paragraph_list = paragraph.split()
    print(paragraph_list)
    for i in paragraph_list:
      if paragraph_list[i] in wordDict: wordDict[word] += 1
      else: wordDict[word] = 1
    return wordDict
print(countWords(paragraph))
#Exercises: Level 2
# 1 Extract values and return their differences
text = """The position of some particles on the horizontal x-axis are -12, -4, -3
 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. 
 Extract these numbers from this whole text and find the distance between the two furthest particles."""
result = re.findall(r"-\d|\d",text)
result = [int(res) for res in result]
result.sort()
print(result[-1] - result[0])
#2 valid python variable
def is_valid_variable(text):
    regex = '^[A-Za-z_][A-Za-z0-9_]*'
    if(re.search(regex, text)):
        print("True")
         
    else:
        print("False")
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True

#Exercises: Level 3
# 1 cleaning out the text and count 3 most frequent words
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(text):
    return re.sub('[&%$@#;,?!.]', '',text)
cleaned_text = clean_text(sentence)

def most_frequent_words(cleaned_text):
    pass
# print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]