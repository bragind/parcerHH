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

def extract_job(html):
  title = html.find('a').text
  link = html.find('a')['href']
  company = html.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).find('a').text
  company = company.strip()
  location = html.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text
  location = location.partition(',')[0]
  return {'title': title, 'company': company, 'location': location, 'link': link}

def extract_hh_jobs(last_page):
  headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'qzip, deflate, br',
  'Connection': 'keep-alive'}
  jobs =[]
  for page in range(last_page):
    print(f'Парсинг страницы {page}')
    result = requests.get(f'{URL}&page={page}', headers = headers)
    print(result.status_code)
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div',{'class': 'serp-item'})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
    
  return jobs


