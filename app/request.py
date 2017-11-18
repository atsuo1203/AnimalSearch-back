from urllib import parse
from urllib import request

from bs4 import BeautifulSoup


def result_print():
    name = parse.quote_plus('ブタ', encoding='utf-8')
    html = request.urlopen('https://ja.wikipedia.org/wiki/' + name).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='borderless')
    return table


print(result_print())
