# combined_file.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class FuncsStuff:
    def __init__(self, soup):
        self.soup = soup

    def _get_data(self):
        dura_l, title_l, desc_l, link_l = [], [], [], []

        parent_tag = self.soup.find_all('article', class_='filmList')
        for i in parent_tag:
            link = i.find('div', class_="filmTitle").find('a')
            title = i.find('div', class_='filmTitle').find('a')
            link_l.append(link.get('href'))
            title_l.append(title.string)

            desc = i.find('p')
            desc_l.append(desc.string)

            dura = i.find('div', class_="runtime")
            dura_l.append(dura.text.strip())

        return dura_l, title_l, desc_l, link_l

    def print_out(self):
        dura, title, desc, link = self._get_data()
        loop_time = len(dura)
        for i in range(loop_time):
            print(title[i])
            print(link[i])
            print(desc[i])
            print(dura[i][:7])
            print('----------------------------------------------------')

def main():
    base_url = "http://www.atmovies.com.tw/movie/new/"
    response = requests.get(base_url)
    response.encoding = 'utf-8'
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    start_up = FuncsStuff(soup)
    start_up.print_out()

if __name__ == "__main__":
    main()
