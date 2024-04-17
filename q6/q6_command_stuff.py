import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

global general_debug
global soup
global url

general_debug = False
title_debug = False
data_debug = True

url = "http://www.atmovies.com.tw/movie/new/"
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'lxml')

#    跳轉到票房排行榜
def start_up():
    rank_scetion = soup.find_all('li')
    section_text = "票房排行榜"    #設定票房排行榜的href的值
    for i in rank_scetion:    #迴圈遍歷一個一個對比
        if general_debug:
            print(i.text.strip())
        if i.text.strip() == section_text:
            link = i.find('a').get('href')
            if link:
                if general_debug:
                    print(link)
                return link

#    混合連結
def link_mix():    #呼叫全域變數 soup 跟 url
    global soup
    global url

    if start_up():
        release = start_up()
        next_url = release
        next_response = requests.get(next_url)
        next_response.encoding = 'utf-8'
        next_html = next_response.text
        soup = BeautifulSoup(next_html, 'lxml')    #修改全域變數soup
    else:
        print("Error:next section link didn't found")
    url = release    #修改全域變數url

#    第二次混和
def second_link_mix():    #跳轉到top20
    global soup    #設定使用全域變數
    view_more = soup.find_all('a')
    view_text = 'twweekend'    #選擇抓取台北的top20

    for i in view_more:
        link = i.get('href')
        try:
            if view_text in link:
                base = url
                result_link = urljoin(base, link)
                break
        except AttributeError:
            print("getting NoneType object in link")

    next_url = result_link
    next_response = requests.get(next_url)
    next_response.encoding = 'utf-8'
    next_html = next_response.text
    soup = BeautifulSoup(next_html, 'lxml')    #修改全域變數


def get_rank():    #抓取排名,寫完後才想到反正排名都是1到20...直接用迴圈生成就好
    rank_list = []
    table = soup.find_all("table")[1]
    trl = table.find_all('tr')

    for i in range(1, len(trl), +2):
        rank = trl[i].find_all('td')[0]
        rank_list.append(rank.text.strip())
    if data_debug:
        print(rank_list)

    return rank_list



def get_title():    #抓取標題
    title_list = []
    table = soup.find_all("table")[1]
    trl = table.find_all('tr')

    for i in range(1, len(trl), +2):
        title = trl[i].find_all('td')[1]
        title_list.append(title.text.strip())
    if data_debug:
        print(title_list)

    return title_list


def get_box():    #抓取票房
    current_box_list = []
    total_box_list = []
    table = soup.find_all("table")[1]
    trl = table.find_all('tr')

    for i in range(2, len(trl), +2):
        current_box = trl[i].find_all('td')[2]
        total_box = trl[i].find_all('td')[3]
        current_box_list.append(current_box.text)
        total_box_list.append(total_box.text)
    if data_debug:
        print("this week box:{}".format(current_box_list))
        print("total box:{}".format(total_box_list))

    return current_box_list, total_box_list

#以下是此代碼的核心部分,不要亂摸會出事
"""        
                             _ooOoo_
                            o8888888o
                            88" . "88
                            (| -_- |)
                            O\  =  /O
                         ____/`---'\____
                       .'  \\|     |//  `.
                      /  \\|||  :  |||//  \\
                     /  _||||| -:- |||||-  \\
                     |   | \\\  -  /// |   |
                     | \_|  ''\---/''  |   |
                     \  .-\__  `-`  ___/-. /
                   ___`. .'  /--.--\  `. . __
                ."" '<  `.___\_<|>_/___.'  >'"".
               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
               \  \ `-.   \_ __\ /__ _/   .-` /  /
          ======`-.____`-.___\_____/___.-`____.-'======
                             `=---='
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                     佛祖保佑        永無BUG
"""
