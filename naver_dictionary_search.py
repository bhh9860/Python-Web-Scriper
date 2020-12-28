import requests
from bs4 import BeautifulSoup
from urllib import parse
urlencoding = '단어'

urlencodings = parse.quote(urlencoding)




html_txt = requests.get(f'https://dict.naver.com/search.nhn?dicQuery={urlencodings}')

html = BeautifulSoup(html_txt.text, 'html.parser')

html_result = html.find('div', {'id' : 'content'})

korean = html_result.find('div', {'class' : 'kr_dic_section'})

a = str(korean.find_all('ul',{'class' : 'lst_krdic'})).replace('\t', '').replace('\r', '').replace('\n', '').split('</li>')

for i in range(len(a)-1):
  a[i].
