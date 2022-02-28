"""Web scrapping"""
# 1 scrapping and store in json file

import json
import requests # importing the request module
from bs4 import BeautifulSoup # importing the request module

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
with open('facts.json', 'a') as facts:
    json.dumps(soup)