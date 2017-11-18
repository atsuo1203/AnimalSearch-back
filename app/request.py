from urllib import parse
from urllib import request

from bs4 import BeautifulSoup


def scientific_name(wiki_name):
    name = parse.quote_plus(wiki_name, encoding='utf-8')
    html = request.urlopen('https://ja.wikipedia.org/wiki/' + name).read()
    soup = BeautifulSoup(html, 'html.parser')
    trs = soup.find('table', class_='borderless').find_all('tr')
    words = [td.find_all('td')[2].find('a') for td in trs]
    last_word = trs[-1].find('b').string
    result_list = [a.string for a in words if a is not None]
    result_list.append(last_word)
    return result_list


# 改行させる
def make_line(li):
    result_word = ''
    for l in li:
        result_word += l
        result_word += '\n'
    return result_word

