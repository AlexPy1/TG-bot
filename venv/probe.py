

from bs4 import BeautifulSoup
import requests
url = 'https://www.sport-express.ru/football/'
page = requests.get(url)
new_news=[]
news=[]
soup=BeautifulSoup(page.content,'html.parser')
news = soup.findAll('a', class_='se19-translation-block__match')

#print(news)
content=[]
for i in range(len(news)):
    if news[i].find('span', class_='se19-translation-block__cell se19-translation-block__cell--team') is not None:
        new_news.append(news[i].text)
for i in range(len(new_news)):
    content.append(new_news[i])
for i in content:
    content_1.add(i)

print(("Сегодня играют:\n{}".format(content)))

