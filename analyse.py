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

import re
#Remplissage du dictionnaire

r = sas = git = java = sql = nbText = 0

for text in texts:
    text = text.lower()
    nbText += 1
    for keyword in keywords:
        if text.find(keyword) >= 0:
            dictKeywords[keyword] += 1
            
    #Regex car il est simple de match avec les mots courts, on fait ces cas à part pour être sûr de leur valeur 
    # (todo mettre dans une fonction)
    regexR = re.search("[^0-9a-zA-ZÀ-ú]r[^0-9a-zA-ZÀ-ú]", text)
    if regexR: r += 1
    regexSas = re.search("[^0-9a-zA-ZÀ-ú]sas[^0-9a-zA-ZÀ-ú]", text)
    if regexSas: sas += 1
    regexGit = re.search("[^0-9a-zA-ZÀ-ú]git[^0-9a-zA-ZÀ-ú]", text)
    if regexGit: git += 1
    regexJava = re.search("[^0-9a-zA-ZÀ-ú]java[^0-9a-zA-ZÀ-ú]", text)
    if regexJava: java += 1
    regexSql = re.search("[^0-9a-zA-ZÀ-ú]sql[^0-9a-zA-ZÀ-ú]", text)
    if regexSql: sql += 1
        
# Puis on insère la valeur dans le dictionnaire
dictKeywords["r"] = r
dictKeywords["sas"] = sas
dictKeywords["git"] = git
dictKeywords["java"] = java
dictKeywords["sql"] = sql

# Regroupement des différentes écritures pour PowerBI en une seule
dictKeywords["power bi"] = dictKeywords["power bi"] + dictKeywords["powerbi"] + dictKeywords["power_bi"] 
dictKeywords["powerbi"] = 0
dictKeywords["power_bi"] = 0

print(dictKeywords)

!pip install wordcloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Génération d'un wordcloud
wordcloud = WordCloud(background_color = "white").generate_from_frequencies(dictKeywords)
plt.imshow(wordcloud)
plt.axis("off")
plt.show();

# Fréquence d'apparition en pourcentage en fonction du nombre d'annonces scrapées
for key, value in dictKeywords.items():
    dictKeywords[key] = (value / nbText)*100
print(dictKeywords)

# Tri
sortedListKeywords = sorted(dictKeywords.items(), key=lambda x: x[1], reverse=True)
sortedKeywords = list(zip(*sortedListKeywords))[0]
sortedValues = list(zip(*sortedListKeywords))[1]

# On n'utilise que les 8 premières valeurs
sortedKeywords = sortedKeywords[:8]
sortedValues = sortedValues[:8]


import matplotlib.pyplot as plt
import numpy

plt.bar(x_pos, sortedValues,align='center')
plt.xticks(x_pos, sortedKeywords) 
plt.ylabel('% d\'apparition du mot par annonce ')
plt.xticks(rotation=45)
plt.show()
