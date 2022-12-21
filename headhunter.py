import requests
from bs4 import BeautifulSoup
URL = 'https://hh.ru/search/vacancy?area=113&experience=noExperience&education=not_required_or_not_specified&search_field=name&search_field=company_name&search_field=description&text=Python&from=suggest_post'

def extract_max_page():
    headers = {
    'Host': 'hh.ru',
    'User-Agent': 'Safari',
    'Accept': '*/*',
    'Accept-Encoding': 'qzip, deflate, br ',
    'Connection': 'keep-alive',
    }

    hh_requests = requests.get(f'{URL}', headers=headers)
    hh_soup = BeautifulSoup(hh_requests.text, 'html.parser')
    pages = []

    paginator = hh_soup.find_all("span",{'class': 'pager-item-not-in-short-range' })

    for page in paginator:
     pages.append(int(page.find('a').text))
 
  return pages[-1]