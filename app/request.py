from urllib import parse
from urllib import request
from urllib import error

from bs4 import BeautifulSoup


def scientific_name(wiki_name):
    name = parse.quote_plus(wiki_name, encoding='utf-8')
    # ページが存在しない時のエラー
    try:
        html = request.urlopen('https://ja.wikipedia.org/wiki/' + name).read()
    except error.HTTPError:
        return ['そのページは存在しません', 'カタカナで試してみてください']

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='borderless')

    if table is None:
        return ['分類が載っていません', 'カタカナで試してみてください', 'それでもダメなら分類が追加されるまで待ちましょう']

    trs = table.find_all('tr')
    words = [td.find_all('td')[2].find('a') for td in trs]
    last_word = trs[-1].find('b').string
    result_list = [a.string for a in words if a is not None]
    if last_word is None:
        return result_list
    result_list.append(last_word)
    return result_list


# 改行させる
def make_line(li):
    result_word = ''
    for l in li:
        result_word += l
        result_word += '\n'
    return result_word

