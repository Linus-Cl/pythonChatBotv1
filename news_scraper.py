import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')
count_headlines = len(headlines)


def get_news_headlines():
    news = []

    for x in headlines:
        if x.text.strip() == "BBC World News TV":
            break

        news.append(x.text.strip())

    del news[0]

    return news


# print(get_news_headlines())
