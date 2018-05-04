
from bs4 import BeautifulSoup
from ezprint import p
import requests
import os

url = 'https://ru.wikipedia.org/wiki/Заглавная_страница'


def get_html(url):
	r = requests.get(url).text
	return r


def parse():
	html = get_html(url)

	soup = BeautifulSoup(html, 'lxml')

	div = soup.find('div', id = 'mf-dyk')

	labels = div.find_all('li')

	for i in labels:
		p(i.getText() + '\n')


if __name__ == '__main__':
	os.system('cls')

	p('Знаете ли вы?')

	p()
	parse()