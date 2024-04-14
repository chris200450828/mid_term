import requests
from bs4 import BeautifulSoup
import q3_command_stuff as qcs

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

history_url = "https://rate.bot.com.tw/xrt/all/day"
history_response = requests.get(history_url)
history_soup = BeautifulSoup(history_response.text, "html.parser")

start_up = qcs.FuncStart(soup, history_soup)
start_up.save_csv(True)
forward_l = start_up.dealed_url()
date_l, buy_l, sell_l = [], [], []
for i in forward_l:
    forward_response = requests.get(i)
    forward_soup = BeautifulSoup(forward_response.text, "html.parser")
    date_l, buy_l, sell_l = start_up.get_forward_data(forward_soup)
    filename = date_l[0][:3].strip()
    result = zip(date_l, buy_l, sell_l)
    start_up.to_forward_csv(filename, result)
