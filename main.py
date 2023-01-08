import requests

headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'qzip, deflate, br',
  'Connection': 'keep-alive'
}
hh_requests = requests.get('https://hh.ru/search/vacancy?text=python&items_on_page=100', headers=headers)

print(hh_requests.text)
