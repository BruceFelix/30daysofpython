"""Packages and how to use them"""
#1 Read from a url and find the 10 most frequent words in romeo_and_juliet
import requests
# from collections import Counter
# response = requests.get("http://www.gutenberg.org/files/1112/1112.txt") # opens network and fetchs data
# text = response.text # we store the information recieved from the url in the variable
# print(Counter(text.split()).most_common(10)) # Counter counts each word that exists in that doc. The most common returns the value that you give it.

#2 Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and
# i the min, max, mean, median, standard deviation of cats' weight in metric units.

response = requests.get("https://api.thecatapi.com/v1/breeds")
print(response.text)