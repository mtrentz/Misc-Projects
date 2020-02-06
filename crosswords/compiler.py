import re
import csv
import pandas as pd
import unidecode

with open('common_last_names.txt', 'r') as file:
    lastnames = file.read().splitlines()

with open('common_first_names.txt', 'r') as file:
    firstnames = file.read().splitlines()

with open('celebrities.txt', 'r') as file:
    celebrities = []
    lines = file.read().splitlines()
    for line in lines:
        line = line.split(',')
        line = line[1:]
        for celebrity in line:
            names = celebrity.split(' ')
            for name in names:
                celebrities.append(name)

with open('celebrities2.txt', 'r') as file:
    celebrities2 = []
    lines = file.read().splitlines()
    for line in lines:
        line = line.split(' ')
        for name in line:
            celebrities2.append(name)

cities = []
w_cities = pd.read_csv('major_cities.txt', encoding='latin1')
for city in w_cities['name']:
    city = city.replace('-', '').replace('.', '').replace(' ', '')
    city = unidecode.unidecode(city)
    cities.append(city)

br_cities = []
b_cities = pd.read_csv('brazil_cities.txt', encoding='latin1', sep='|')
for city in b_cities['Cidade']:
    city = city.replace('-', '').replace('.', '').replace(' ', '')
    city = unidecode.unidecode(city)
    br_cities.append(city)


with open('palavras.txt', 'r', encoding='utf8') as file:
    palavras = []
    lines = file.read().splitlines()
    for line in lines:
        line = line.replace('-', '').replace('.', '')
        line = unidecode.unidecode(line)
        palavras.append(line)


with open('words_db.txt', 'w') as file:
    for name_list in [lastnames, firstnames, celebrities, celebrities2, cities, br_cities, palavras]:
        for name in name_list:
            file.write(name+'\n')


