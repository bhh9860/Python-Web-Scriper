import requests
from bs4 import BeautifulSoup
from urllib import parse
urlencoding = '가나다'

urlencodings = parse.quote(urlencoding)




html_txt = requests.get(f'https://dict.naver.com/search.nhn?dicQuery={urlencodings}')

html = BeautifulSoup(html_txt.text, 'html.parser')

html_result = html.find('div', {'id' : 'content'})

korean = html_result.find('div', {'class' : 'kr_dic_section'})

korean_soup = korean.find_all('ul',{'class' : 'lst_krdic'}).li
