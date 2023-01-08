import requests
from bs4 import BeautifulSoup

ITEMS = 100
URL = f'https://hh.ru/search/vacancy?text=python&items_on_page={ITEMS}'
headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'qzip, deflate, br',
  'Connection': 'keep-alive'}

def extract_max_page():
  headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'qzip, deflate, br',
  'Connection': 'keep-alive'}
  
  hh_requests = requests.get(URL, headers = headers)
  hh_soup = BeautifulSoup(hh_requests.text, 'html.parser')

  pages = []

  paginator = hh_soup.find_all("span", {'class': 'pager-item-not-in-short-range'})

  for page in paginator:
    pages.append(int(page.find('a').text))

  return pages[-1]

def extract_hh_jobs(last_page):
  headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'qzip, deflate, br',
  'Connection': 'keep-alive'}
  jobs =[]
  #for page in range(last_page):
  result = requests.get(f'{URL}&page=0', headers = headers)
  print(result.status_code)
  soup = BeautifulSoup(result.text, 'html.parser')
  results = soup.find_all('span',{'class': 'vacancy_search_suitable_item'})
  for result in results:
    print(result.find('a').text)
    
  return jobs


