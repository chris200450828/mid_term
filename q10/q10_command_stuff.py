import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import datetime
from datetime import datetime, timedelta
import json
import os

global soup
global date
global general
global apply_date

global adv_link
adv_link = False

today = datetime.today()
yesterday = today - timedelta(days=1)
yesterday = yesterday.strftime("%m/%d").lstrip("0")
date = today.strftime("%m/%d").lstrip("0")

time_buffer = 300

general_debug = False
dc_debug = False
cd_debug = False
lm_debug = False
gd_debug = False
gd_adv_debug = False

url = "https://www.ptt.cc/bbs/NBA/index.html"
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'lxml')

general = soup.find_all("div", class_='r-ent')


def day_manager(opt=None):  # a prevention of 00:01 that cause no data found
    global apply_date
    if opt is None:
        apply_date = date
        print("advance day manager is off,will use today's forum,using {} as date variable".format(date))
        print("=====================================")
    elif opt == True:
        print("applying advance day manager")
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        total_minute = (hour * 60) + minute
        if total_minute > time_buffer:
            apply_date = date
            print("5 hours past, using today's date as criterion,using {} as date variable".format(date))
            print("=====================================")
        else:  # will grab data if it is before 05:00
            apply_date = yesterday
            print("using yesterday's date as criterion, using {} as date variable".format(yesterday))
            print("=====================================")
    else:
        apply_date = date
        print("advance day manager is off,will use today's forum,using {} as date variable".format(date))
        print("=====================================")


day_manager()


def date_check(grand=None):
    if grand is None:  # basically for debug purpose,will print out all the date
        for i in general:
            meta = i.find("div", class_='meta')
            date = meta.find("div", class_='date')
            if general_debug or dc_debug:
                print(date)
    else:
        meta = grand.find("div", class_='meta')
        date_ = meta.find("div", class_='date')
        if general_debug or dc_debug:
            print(date.text.strip())
            print(apply_date)
        if date_.text.strip() == apply_date:
            return True
        else:
            return False


def get_author(i):
    meta = i.find("div", class_='meta')
    author = meta.find("div", class_='author')
    return author.text


def get_title(i):
    try:
        title_parent = i.find("div", class_='title')
        title = title_parent.find('a')
        return title.text
    except AttributeError as deleted_forum:
        title = i.find("div", class_='title')
        return title.text
    except Exception as NonetypeError:
        return "nothing found"


def get_link(i):
    try:
        link_parent = i.find("div", class_='title')
        link_element = link_parent.find('a')
        link = link_element.get('href')
        return link
    except AttributeError as NonetypeError:
        return " "


def get_push(i):
    try:
        try:
            push_parent = i.find("div", class_='nrec')
            push = push_parent.find("span", class_='hl f3')
            return push.text
        except AttributeError as h3:
            push_parent = i.find("div", class_='nrec')
            try:
                push = push_parent.find("span", class_='hl f1')
                return push.text
            except AttributeError as h2:
                push = push_parent.find("span", class_='hl f2')
                return push.text
    except AttributeError as NonetypeError:
        return " "


def advance_link_mode(opt=None, pop=None):
    global adv_link
    if opt == True:
        if pop:
            print("using advance link mode")
            print("=====================================")
        adv_link = True
    else:
        adv_link = False


def file_exist_checker():
    file = "article.json"
    if os.path.isfile(file):
        print("File exist,process failed")
        return False
    else:
        return True


def link_mix(original_link):
    base = url
    addon = original_link
    link_result = urljoin(base, addon)
    if lm_debug:
        print(link_result)
    return link_result


def get_data():
    author_list, title_list, push_list, link_list = [], [], [], []
    for i in general:
        if date_check(i) == True:
            author = get_author(i)
            title = get_title(i)
            push = get_push(i)
            if adv_link:
                link = link_mix(get_link(i))
            else:
                link = get_link(i)

            author_list.append(author)
            title_list.append(title)
            push_list.append(push)
            link_list.append(link)

            if general_debug or gd_adv_debug:
                print(author)
                print(title)
                print(push)
                print(link)
                print('--------------')

            data_list = []
            data_zip = zip(author_list, title_list, push_list, link_list)
            for author, title, push, link in data_zip:
                data_list.append({
                    "author": author,
                    "title": title,
                    "push_count": push,
                    "href": link
                })
    return data_list


def advance_file_manager(data_list, opt=None):
    if opt == True:
        save_day = today.strftime("%Y_%m_%d")
        file = save_day + '_article.json'
        json_string = json.dumps(data_list, ensure_ascii=False)
        with open(file, "w", encoding='utf-8') as json_file:
            json_file.write(json_string)
        print("done")
    else:
        json_string = json.dumps(data_list, ensure_ascii=False)
        with open('article.json', "w", encoding='utf-8') as json_file:
            json_file.write(json_string)
        print("done")

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import datetime
from datetime import datetime, timedelta
import json
import os

global soup
global date
global general
global apply_date

global adv_link
adv_link = False

today = datetime.today()
yesterday = today - timedelta(days=1)
yesterday = yesterday.strftime("%m/%d").lstrip("0")
date = today.strftime("%m/%d").lstrip("0")

time_buffer = 300

general_debug = False
dc_debug = False
cd_debug = False
lm_debug = False
gd_debug = False
gd_adv_debug = False

url = "https://www.ptt.cc/bbs/NBA/index.html"
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'lxml')

general = soup.find_all("div", class_='r-ent')


def day_manager(opt=None):  # a prevention of 00:01 that cause no data found
    global apply_date
    if opt is None:
        apply_date = date
        print("advance day manager is off,will use today's forum,using {} as date variable".format(date))
        print("=====================================")
    elif opt == True:
        print("applying advance day manager")
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        total_minute = (hour * 60) + minute
        if total_minute > time_buffer:
            apply_date = date
            print("5 hours past, using today's date as criterion,using {} as date variable".format(date))
            print("=====================================")
        else:  # will grab data if it is before 05:00
            apply_date = yesterday
            print("using yesterday's date as criterion, using {} as date variable".format(yesterday))
            print("=====================================")
    else:
        apply_date = date
        print("advance day manager is off,will use today's forum,using {} as date variable".format(date))
        print("=====================================")


day_manager()


def date_check(grand=None):
    if grand is None:  # basically for debug purpose,will print out all the date
        for i in general:
            meta = i.find("div", class_='meta')
            date = meta.find("div", class_='date')
            if general_debug or dc_debug:
                print(date)
    else:
        meta = grand.find("div", class_='meta')
        date_ = meta.find("div", class_='date')
        if general_debug or dc_debug:
            print(date.text.strip())
            print(apply_date)
        if date_.text.strip() == apply_date:
            return True
        else:
            return False


def get_author(i):
    meta = i.find("div", class_='meta')
    author = meta.find("div", class_='author')
    return author.text


def get_title(i):
    try:
        title_parent = i.find("div", class_='title')
        title = title_parent.find('a')
        return title.text
    except AttributeError as deleted_forum:
        title = i.find("div", class_='title')
        return title.text
    except Exception as NonetypeError:
        return "nothing found"


def get_link(i):
    try:
        link_parent = i.find("div", class_='title')
        link_element = link_parent.find('a')
        link = link_element.get('href')
        return link
    except AttributeError as NonetypeError:
        return " "


def get_push(i):
    try:
        try:
            push_parent = i.find("div", class_='nrec')
            push = push_parent.find("span", class_='hl f3')
            return push.text
        except AttributeError as h3:
            push_parent = i.find("div", class_='nrec')
            try:
                push = push_parent.find("span", class_='hl f1')
                return push.text
            except AttributeError as h2:
                push = push_parent.find("span", class_='hl f2')
                return push.text
    except AttributeError as NonetypeError:
        return " "


def advance_link_mode(opt=None, pop=None):
    global adv_link
    if opt == True:
        if pop:
            print("using advance link mode")
            print("=====================================")
        adv_link = True
    else:
        adv_link = False


def file_exist_checker():
    file = "article.json"
    if os.path.isfile(file):
        print("File exist,process failed")
        return False
    else:
        return True


def link_mix(original_link):
    base = url
    addon = original_link
    link_result = urljoin(base, addon)
    if lm_debug:
        print(link_result)
    return link_result


def get_data():
    author_list, title_list, push_list, link_list = [], [], [], []
    for i in general:
        if date_check(i) == True:
            author = get_author(i)
            title = get_title(i)
            push = get_push(i)
            if adv_link:
                link = link_mix(get_link(i))
            else:
                link = get_link(i)

            author_list.append(author)
            title_list.append(title)
            push_list.append(push)
            link_list.append(link)

            if general_debug or gd_adv_debug:
                print(author)
                print(title)
                print(push)
                print(link)
                print('--------------')

            data_list = []
            data_zip = zip(author_list, title_list, push_list, link_list)
            for author, title, push, link in data_zip:
                data_list.append({
                    "author": author,
                    "title": title,
                    "push_count": push,
                    "href": link
                })
    return data_list


def advance_file_manager(data_list, opt=None):
    if opt == True:
        save_day = today.strftime("%Y_%m_%d")
        file = save_day + '_article.json'
        json_string = json.dumps(data_list, ensure_ascii=False)
        with open(file, "w", encoding='utf-8') as json_file:
            json_file.write(json_string)
        print("done")
    else:
        json_string = json.dumps(data_list, ensure_ascii=False)
        with open('article.json', "w", encoding='utf-8') as json_file:
            json_file.write(json_string)
        print("done")



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
