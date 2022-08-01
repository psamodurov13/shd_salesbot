import requests
from bs4 import BeautifulSoup as bs
import json

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
                  '(KHTML, like Gecko) Version/15.5 Safari/605.1.15'
}


def get_page(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    with open('index.html', 'w') as file:
        file.write(response.text)


def collect_data(url):
    s = requests.Session()
    print('start')
    response = s.get(url=url, headers=headers)
    data = bs(response.text, features='html.parser')
    print('data')
    if data.select('ul.pagination > li > a'):
        last_page = str(data.select('ul.pagination > li > a')[-1]).replace('">&gt;|</a>', '')
        res = int(last_page.split('?page=')[-1])
        print('count-pages')
    else:
        res = 1
    print(f'Количество страниц: {res}')
    return res


def get_urls(url, page):
    s = requests.Session()
    print(f'page {page}')
    response = s.get(url=f'{url}/?page={page}', headers=headers)
    data = bs(response.text, features='html.parser')
    products_on_page = [el['href'] for el in data.select('.product-thumb .image a[href]')]
    return products_on_page


def get_prod_info(products_on_page, category):
    s = requests.Session()
    i = 0
    for product in products_on_page:
        print(f'product {i}/{len(products_on_page)}')
        response = s.get(url=product, headers=headers)
        data = bs(response.text, features='html.parser')
        yield [data.select('h1.item-header')[0].text, product,
               data.select('div.right-info p.price-old')[0].text,
               data.select('div.right-info div.price')[0].text,
               ', '.join(item.get_text().strip() for item in data.find_all('label', class_='optid-11'))]
        i += 1
        print(f'Обработано: {i} из {len(products_on_page)}')


def main():
    collect_data()


if __name__ == '__main__':
    main()