import requests
import urllib.request
from bs4 import BeautifulSoup

result = requests.get('https://finance.naver.com/sise/lastsearch2.nhn')

soup = BeautifulSoup(result.text, 'html.parser')


stocks = []
for i in soup.find_all('tr'):
  stocks.append(i)
stocks = list(filter(None, stocks))

num = [1, 3, 4, 5]

names = []
percentages = []
up_down = []
for i in stocks[7:52]:
  temper = str(i)
  temper.split('</td>')[1]
 #names.append(temper[1].split('>')[2])
#7~51
