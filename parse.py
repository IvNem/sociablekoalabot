import requests
import urllib
from bs4 import BeautifulSoup as BS


def parse(flag):
    if flag == 'img1':
        URL = 'https://cardrise.ru/category/otkrytki-i-kartinki-s-pozhelaniyami/otkrytki-i-kartinki-horoshego-nastroeniya/'
    elif flag == 'img2':
        URL = 'https://cardrise.ru/category/otkrytki-i-kartinki-s-pozhelaniyami/otkrytki-i-kartinki-dobrogo-i-horoshego-dnya/'
    elif flag == 'img3':
        URL = 'https://cardrise.ru/category/otkrytki-i-kartinki-s-pozhelaniyami/otkrytki-i-kartinki-s-dobrym-utrom/'
    elif flag == 'img4':
        URL = 'https://cardrise.ru/category/otkrytki-i-kartinki-s-pozhelaniyami/otkrytki-i-kartinki-spokoynoy-nochi/'
    HEADERS = {
        # User-Agent нужен чтобы сайт не посчитал нас ботом
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    # Получаем содержимое страницы по ссылке
    response = requests.get(URL, headers=HEADERS)
    # Полученную страницу отправляем на обработку в суп
    soup = BS(response.content, 'html.parser')
    items = soup.findAll('div', class_='post-thumbnail-container')
    comps = []

    for i in items:
        comps.append({
            # Создаем ключ
            'title': i.find('a', class_='responsive-featured-image').get('title'),
            'link': i.find('img', class_='post-featured-image').get('src')
        })
    for comp in comps:
        print(f'{comp["title"]} -> Link: {comp["link"]}')
    return comps


def load_image(random_comp):
    f = open('out.jpg', 'wb')
    f.write(urllib.request.urlopen(random_comp["link"]).read())
    f.close()
