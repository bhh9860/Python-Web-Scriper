import requests
from bs4 import BeautifulSoup

html_txt = requests.get('https://weather.naver.com/today/05200102')

html = BeautifulSoup(html_txt.text, 'html.parser')

one = html.find('div', {'id' : 'wrap'})

temperature = one.find('strong', {'class' : 'current'}).text.split(' ')[1].replace('온도', '')
