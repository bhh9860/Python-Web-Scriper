import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='

plusUrl = input('검색어 : ')
url = baseUrl + urllib.parse.quote_plus(plusUrl)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='api_txt_lines')

for i in range(0, len(title), 2):
  print(title[i].text.strip())
