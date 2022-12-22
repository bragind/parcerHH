import requests
from bs4 import BeautifulSoup
headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive'
}
hh_request = requests.get('https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python&excluded_text=&area=113&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=100', headers=headers)
hh_soup = BeautifulSoup(hh_request.text, 'html.parser')

paginator = hh_soup.find("span", {'class':'bloko-button_pressed'})

pages = paginator.find_all('a')
print(pages)
