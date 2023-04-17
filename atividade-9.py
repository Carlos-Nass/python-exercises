import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
pag = requests.get(url)
soup = BeautifulSoup(pag.content, "html.parser")

titles = soup.find_all(class_="css-1qwxefa esl82me1")

with open("titulos_nytimes.txt", "w") as arq:
    for title in titles:
        arq.write(title.text + "\n")