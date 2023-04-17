import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
pagina = requests.get(url)
soup = BeautifulSoup(pagina.content, "html.parser")

titles = soup.find_all(class_="css-1qwxefa esl82me1")

for title in titles:
    print(title.text)