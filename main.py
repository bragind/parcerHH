import requests
from bs4 import BeautifulSoup
headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'qzip, deflate, br',
  'Connection': 'keep-alive'
}
hh_requests = requests.get('https://hh.ru/search/vacancy?text=python&items_on_page=100', headers=headers)
hh_soup = BeautifulSoup(hh_requests.text, 'html.parser')

pages = []

paginator = hh_soup.find_all("span", {'class': 'pager-item-not-in-short-range'})

for page in paginator:
  pages.append(int(page.find('a').text))


print(pages)
