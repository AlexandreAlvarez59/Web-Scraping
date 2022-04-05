import requests
from bs4 import BeautifulSoup
import time

links = []
vjk = '&vjk=e89ea64923a83e9f'

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
