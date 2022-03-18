"""Web scrapping"""
# 1 scrapping and store in json file

import json
from textwrap import indent
import requests # importing the request module
from bs4 import BeautifulSoup # importing the request module
# Question 1
# url = 'http://www.bu.edu/president/boston-university-facts-stats/'
# response = requests.get(url)
# content = response.content
# soup = BeautifulSoup(content, 'html.parser')
# soup_json = json.dumps(str(soup), indent = 4)
# with open('facts.json', 'w') as facts:
#     facts.write(soup_json)  ALL READY WORKS

# Question 2
# response = requests.get("https://archive.ics.uci.edu/ml/datasets.php")
# content = response.content
# soup = BeautifulSoup(content, 'html.parser')
# tables = soup.find_all('table')
# tables_to_json = json.dumps(str(tables), indent=4)

# with open('tables.json', 'w') as tables_json:
#     tables_json.write(tables_to_json) Also works

# Question 3
response = requests.get("https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States")
content = response.content
soup = BeautifulSoup(content, 'html.parser')
tables = soup.find('table', {'class': "wikitable"})
tables_to_json = json.dumps(str(tables), indent = 4)

with open('presidentstables.json', 'w') as tables_json:
    tables_json.write(tables_to_json)