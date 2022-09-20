from bs4 import BeautifulSoup
import requests
url = 'https://www.ukr.net/ua/news/odesa.html'
url_news = 'https://www.ukr.net/news/science.html'
r = requests.get(url_news)
soup = BeautifulSoup(r.content, 'html.parser')
articles_cards = soup.find_all('article')
for article in articles_cards:
 
  article_desk = article.find('section', class_ = 'im' ).text.strip()
  print( article_desk)