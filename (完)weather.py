import requests
from bs4 import BeautifulSoup

html_txt = requests.get('https://weather.naver.com/today/05110101')

html = BeautifulSoup(html_txt.text, 'html.parser')

weather = html.find('div', {'id' : 'wrap'})

temperature = weather.find('strong', {'class' : 'current'}).text.split(' ')[1].replace('온도', '')

weather_2 = weather.find('dl', {'class' : 'summary_list'}).text.replace('\n', ' ').strip().split(' ')

print('현재온도' + ' ' + temperature)
for i in range(0, len(weather_2), 2):
  print(weather_2[i] + ' ' + weather_2[i+1])
