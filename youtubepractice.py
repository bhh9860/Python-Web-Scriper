import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.youtube.com/playlist?list=PLW7D-oXvDUP2OJASZn1nOuSeAlv9KuZwp')

soup = BeautifulSoup(result.text, 'html.parser')

print(soup.find_all(id='content'))
