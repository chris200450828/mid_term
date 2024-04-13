from bs4 import BeautifulSoup
import requests
import q2_command_stuff as qcs

url = "https://www.ptt.cc/bbs/NBA/index.html"
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'lxml')

start = qcs.FuncStuff(soup)
start.print_out()
