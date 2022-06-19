import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
'Accept-Language': 'ru-RU,ru;q=0.9',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Cache-Control': 'max-age=0',
'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
'sec-ch-ua-mobile': '?0'
}

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

base_url = 'https://habr.com'
url = base_url + '/ru/all'

response = requests.get(url, headers=HEADERS)
text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.findAll('article')

links = [article.find(class_='tm-article-snippet__title-link').get('href') for article in articles]

for link in links:
    response = requests.get(base_url+link, headers=HEADERS)
    text = response.text
    soup = BeautifulSoup(text, features='html.parser')
    article = soup.find('article')
    article_text = article.text
    article_name = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h1').text
    date_of_publication = article.find('time').get('title')[:10]
    article_words = re.sub(r"[\s\d;:?”.,*!“'\"–-]+", r' ', article_text).split()
    article_words_lower_case = (word.lower() for word in article_words)
    if set(KEYWORDS) & set(article_words_lower_case):
        print(f'{date_of_publication} - {article_name} - {base_url}{link}')





