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


def collect_data(category=''):
    s = requests.Session()
    response = s.get(url='https://sweethomedress.ru/specials/', headers=headers)
    data = bs(response.text, features='html.parser')
    if data.select('ul.pagination > li > a'):
        last_page = str(data.select('ul.pagination > li > a')[-1]).replace('">&gt;|</a>', '')
        res = int(last_page.split('?page=')[-1])
    else:
        res = 1
    print(f'Количество страниц: {res}')
    products = []
    for page in range(1, res + 1):
        response = s.get(url=f'https://sweethomedress.ru/specials/?page={page}', headers=headers)
        data = bs(response.text, features='html.parser')
        products.extend([el['href'] for el in data.select('.product-thumb .image a[href]')])

    results = []
    i = 0
    for product in products:
        response = s.get(url=product, headers=headers)
        data = bs(response.text, features='html.parser')
        cats = data.select('.catprod a')
        if category in [el.get_text() for el in cats]:
            results.append(
                {
                    'title': data.select('h1.item-header')[0].text,
                    'url': product,
                    'old_price': data.select('div.right-info p.price-old')[0].text,
                    'new_price': data.select('div.right-info div.price')[0].text,
                    'size': ', '.join(item.get_text().strip() for item in data.find_all('label', class_='optid-11'))
                }
            )
        i += 1
        print(f'Обработано: {i} из {len(products)}')
    print(results)
    with open('results.json', 'w') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)


def main():
    collect_data()


if __name__ == '__main__':
    main()