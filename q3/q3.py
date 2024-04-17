import requests
from bs4 import BeautifulSoup
import q3_command_stuff as qcs

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

history_url = "https://rate.bot.com.tw/xrt/all/day"
history_response = requests.get(history_url)
history_soup = BeautifulSoup(history_response.text, "html.parser")

start_up = qcs.FuncStart(soup, history_soup)    #初始化類別
start_up.save_csv(True)    #選擇將資料分開儲存,若不希望分開儲存可以直接在括號內不輸入變數即可
forward_l = start_up.dealed_url()    #呼叫處理遠期匯率連結的變數
date_l, buy_l, sell_l = [], [], []
for i in forward_l:    #迴圈遍歷以抓取遠期匯率的資料
    forward_response = requests.get(i)
    forward_soup = BeautifulSoup(forward_response.text, "html.parser")
    date_l, buy_l, sell_l = start_up.get_forward_data(forward_soup)
    filename = date_l[0][:3].strip()    #選用幣值名稱當作檔案名稱
    result = zip(date_l, buy_l, sell_l)
    start_up.to_forward_csv(filename, result)
