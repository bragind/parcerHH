import requests
from bs4 import BeautifulSoup
ITEMS = 100
URL = 'https://hh.ru/search/vacancy?st=searchVacancy&text=python&items_on_page={ITEMS}' 

headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive'
}
def extract_max_page():
  

  hh_request = requests.get(URL, headers=headers)

  hh_soup = BeautifulSoup(hh_request.text, 'html.parser')

  pages = []

  paginator = hh_soup.find_all("span", {'class':'pager-item-not-in-short-range'})

  for page in paginator:
    pages.append(int(page.find('a').text))



  return  pages[-1]
def extract_hh_jobs(last_page):
  for page in range(last_page):
     result = requests.get(f'{URL}&page={page}',headers=headers)
     print(result.status_code)
  
