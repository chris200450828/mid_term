import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

general_debug = False


#    定義啟動器,接收一個陣列
def start_up(team):
    url_List = []
    url_front = "https://www.basketball-reference.com/teams/"
    url_back = "/2024.html"
    for i in team:
        url_result = url_front + i + url_back
        url_List.append(url_result)

    return url_List


#    接收一個stirng
def get_soup(target_url):
    response = requests.get(target_url)
    response.encoding = 'utf-8'
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    return soup


#    接收soup
def get_data(soup):
    team_name_l, num_l, name_l, pos_l, ht_l, wt_l, exp_l, college_l, birth_l = [], [], [], [], [], [], [], [], []
    i = 0

    table_parent = soup.find("table", class_="sortable")
    table = table_parent.find("tbody")
    data = table.find_all("tr")
    for i in data:
        num = i.find("th", {'data-stat': "number"})
        if num.text == '' or num.text is None:
            num_l.append("NULL")
        else:
            num_l.append(num.text)

        team_name_parent = soup.find("div", {'data-template': 'Partials/Teams/Summary'})
        team = team_name_parent.find('h1').find_all('span')[1]
        team_name_l.append(team.text)

        name_grand = i.find("td", {'data-stat': "player"})
        name_parent = name_grand.find("a")
        name_l.append(name_parent.text)

        pos = i.find("td", {'data-stat': "pos"})
        pos_l.append(pos.text)

        ht = i.find("td", {'data-stat': "height"})
        height_text = ht.text
        height_text_f = height_text[:1] + '=' + height_text[2:]
        ht_l.append(height_text_f)

        wt = i.find("td", {'data-stat': "weight"})
        wt_l.append(wt.text)

        exp = i.find("td", {'data-stat': "years_experience"})
        exp_l.append(exp.text)

        try:
            college_parent = i.find("td", {'data-stat': "college"})
            college = college_parent.find('a')
            college_l.append(college.text)
        except AttributeError as double_layer_elemnet:
            college = 'NULL'
            college_l.append(college)

        birth = i.find("td", {'data-stat': "birth_date"})
        birth_l.append(birth.text)

    result = zip(num_l, name_l, pos_l, ht_l, wt_l, exp_l, college_l, birth_l, team_name_l)
    return result
