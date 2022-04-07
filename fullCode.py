#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import time

links = []
vjk = '&vjk=e89ea64923a83e9f'

## Récupération des URLs de chaque annonce

for i in range(0, 71, 10):
    startUrl = '&start='+str(i)
    if i == 0:
        startUrl=vjk
    url = 'https://fr.indeed.com/jobs?q=Data%20analyst%20junior&l=France'+startUrl
    print(url)
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Récupération de la liste des annonces contenant le lien
        allAs = soup.select('.jobTitle > a')
        for a in allAs:
            link = a['href']
            print(link)
            links.append('https://fr.indeed.com'+link)
        time.sleep(3)

    with open('urls.txt','w') as file:
        for link in links: 
            file.write(link + '\n')


# In[2]:


import requests
from bs4 import BeautifulSoup
import time

texts = []

## Récupération du texte de chaque annonce

with open('urls.txt', 'r') as file:
    for row in file:
        # Some links seems to be ads, let's remove it
        if row[:25] == 'https://fr.indeed.com/rc/':
            response = requests.get(row)
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                jobText = soup.select('#jobDescriptionText')
                strSoup = soup.text
                texts.append(strSoup)
                time.sleep(3)


# In[3]:


#Liste de mots clés à rechercher

keywords = ['excel', 'sql', 'microsoft', 'tableau',  'python', 'word', 'powerpoint', 'r',  'slack', 'looker', 'azure', 'jira', 'server', 'snowflake', 'scrum',
'powerbi', 'shell', 'linux', 'sas', 'sharepoint', 'devops', 'mysql', 'javascript', 'mssql', 'vba', 'postgresql', 'spreadsheets',
'pandas', 'gdpr', 'rgpd' 'elt', 'scala', 'css', 'spreadsheet', 'alteryx', 'git', 'github', 'postgres', 'power_bi', 'spss', 'power', 'cloud', 'saas', 'etl', 
            'hadoop', 'dataviz', 'visualisation', 'programmation', 'gcp', 'aws', 'docker', 'html']

lenK = len(keywords)
lZeros = [0] * lenK

#Création d'un dictionnaire avec chaque mot clé initialisé à 0

dictKeywords = dict(zip(keywords, lZeros))
print(dictKeywords)


# In[4]:


import re
#Remplissage du dictionnaire

r = sas = git = nbText = 0


for text in texts:
    text = text.lower()
    nbText += 1
    for keyword in keywords:
        if text.find(keyword) >= 0:
            dictKeywords[keyword] += 1
            
    #Regex car il est simple de match avec les mots courts, on fait ces cas à part pour être sûr de leur valeur
    regexR = re.search("[^0-9a-zA-ZÀ-ú]r[^0-9a-zA-ZÀ-ú]", text)
    if regexR: r += 1
    regexSas = re.search("[^0-9a-zA-ZÀ-ú]sas[^0-9a-zA-ZÀ-ú]", text)
    if regexSas: sas += 1
    regexGit = re.search("[^0-9a-zA-ZÀ-ú]git[^0-9a-zA-ZÀ-ú]", text)
    if regexGit: git += 1
        
# Puis on insère la valeur dans le dictionnaire
dictKeywords["r"] = r
dictKeywords["sas"] = sas
dictKeywords["git"] = git
dictKeywords["java"] = git

print(dictKeywords)


# In[5]:


get_ipython().system('pip install wordcloud')


# In[6]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Génération d'un wordcloud
wordcloud = WordCloud(background_color = "white").generate_from_frequencies(dictKeywords)
plt.imshow(wordcloud)
plt.axis("off")
plt.show();


# In[7]:


# Fréquence d'apparition en pourcentage en fonction du nombre d'annonces scrapées
for key, value in dictKeywords.items():
    dictKeywords[key] = (value / nbText)*100
print(dictKeywords)


# In[8]:


# Tri
sortedListKeywords = sorted(dictKeywords.items(), key=lambda x: x[1], reverse=True)
sortedKeywords = list(zip(*sortedListKeywords))[0]
sortedValues = list(zip(*sortedListKeywords))[1]

# On n'utilise que les 8 premières valeurs
sortedKeywords = sortedKeywords[:8]
sortedValues = sortedValues[:8]


# In[9]:

import matplotlib.pyplot as plt
import numpy

plt.bar(x_pos, sortedValues,align='center')
plt.xticks(x_pos, sortedKeywords) 
plt.ylabel('% d\'apparition du mot par annonce ')
plt.xticks(rotation=45)
plt.show()

