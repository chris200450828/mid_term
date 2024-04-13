import requests
from bs4 import BeautifulSoup
import q1_command_stuff as qcs
from urllib.parse import urljoin

base_url = "http://www.atmovies.com.tw/movie/new/"
response = requests.get(base_url)
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'lxml')

start_up = qcs.FuncsStuff(soup)
start_up.print_out()
