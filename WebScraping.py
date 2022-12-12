from bs4 import BeautifulSoup
import requests
site = requests.get('http://172.217.173.100/').content
soup = BeautifulSoup(site, 'html.parser')
#print(soup.prettify())
print(soup.script.string)
