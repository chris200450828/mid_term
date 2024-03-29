import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

global soup
general_debug = False
gr_debug = False
lm_debug = False
grd_debug = False

url = "http://www.atmovies.com.tw/movie/new/"
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'lxml')


def get_release():
    movie_scetion = soup.find_all('li')
    section_text = "近期上映"
    for i in movie_scetion:
        if general_debug or gr_debug:
            print(i.text.strip())
        if i.text.strip() == section_text:
            link = i.find('a').get('href')
            if link:
                if general_debug or gr_debug:
                    print(link)
                return link


def link_mix():
    global soup
    if get_release():
        base = "http://www.atmovies.com.tw/movie/new/"
        release = get_release()
        dest = urljoin(base, release)
        if general_debug or lm_debug:
            print(dest)
        next_url = dest
        next_response = requests.get(next_url)
        next_response.encoding = 'utf-8'
        next_html = next_response.text
        soup = BeautifulSoup(next_html, 'lxml')
    else:
        print("Error:next section link didn't found")


def get_release_data():
    result, link_list, date_list, name_list = [], [], [], []
    date = soup.find_all("div", class_='runtime')
    name = soup.find_all("div", class_="filmtitle")
    link_grand_parent = soup.find('ul', class_='filmListAllX')
    link_parent = link_grand_parent.find_all('li')
    for i in range(0, len(name)):
        name_list.append(name[i].text)
        date_clean = re.sub(r"\n.*", "", date[i].text)
        date_clean = re.sub(r"\r.*", "", date_clean)
        date_list.append(date_clean)
    for i in link_parent:
        link = i.find('a')
        link = link.get('href')
        base = "http://www.atmovies.com.tw/movie/new/"
        final_link = urljoin(base, link)
        link_list.append(final_link)
        if general_debug or grd_debug:
            print(final_link)

    result = zip(name_list, date_list, link_list)
    for i in result:
        print(i)
    return result

