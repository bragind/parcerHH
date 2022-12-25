import requests
from bs4 import BeautifulSoup

headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive'
}

hh_request = requests.get('https://hh.ru/search/vacancy?&items_on_page=100&st=searchVacancy&text=python', headers=headers)

hh_soup = BeautifulSoup(hh_request.text, 'html.parser')

pages = []

paginator = hh_soup.find_all("span", {'class':'pager-item-not-in-short-range'})

for page in paginator:
  pages.append(int(page.find('a').text))


max_page = pages[-1]
for page in range(max_page):
  print(f'page={page}')

