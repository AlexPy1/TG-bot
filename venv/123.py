import requests
r= requests.get("https://www.sport-express.ru/football/")
print(r)
from bs4 import BeautifulSoup

class HabrPythonNews(str):

    def __init__(self):
        self.url = 'https://www.sport-express.ru/football/'
        self.html = self.get_html()

    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False

    def replace(self, *args, **kwargs):  # real signature unknown
        pass


    def get_python_news(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        news_list = soup.findAll('span', class_="se19-translation-block__cell se19-translation-block__cell--team")

        return news_list
if __name__ == "__main__":
    news = HabrPythonNews()
    print(news.get_python_news())