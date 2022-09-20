from bs4 import BeautifulSoup
import requests
url = 'https://www.archaeology.org'
url_news = 'https://www.archaeology.org/news'
r = requests.get(url_news)
soup = BeautifulSoup(r.content, 'html.parser')
articles_cards = soup.find_all('div', class_ = 'news_intro')

for article in articles_cards:
  article_title = article.find('a', href = True).text.strip()
  article_desk = article.find('p', class_ = 'news_cont').text.strip()
  print(article_title, article_desk)
  url = 'https://www.archaeology.org'
url_news_2 = 'https://www.archaeology.org/news?page=2'
r = requests.get(url_news)
soup = BeautifulSoup(r.content, 'html.parser')
articles_cards = soup.find_all('div', class_ = 'news_intro')

for article in articles_cards:
  article_title = article.find('a', href = True).text.strip()
  article_desk = article.find('p', class_ = 'news_cont').text.strip()
  print(article_title, article_desk)
