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