import requests
from bs4 import BeautifulSoup
import csv

url = "https://search.books.com.tw/search/query/key/演算法/cat/all"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 開啟 CSV 檔案，並建立 csv 寫入物件，使用 utf-8-sig 編碼
with open('booklist.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    # 定義 CSV 欄位名稱
    fieldnames = ['書名', '網址', '作者', '書價']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入欄位名稱
    writer.writeheader()

    # 尋找每本書的資料，並寫入 CSV 檔案
    title_text = soup.find_all("div", class_="table-td")
    for i in title_text:
        try:
            title_t = i.find("h4").find("a")
            book_title = title_t.get('title')
            book_url = title_t.get('href')
        except AttributeError as NoneTypeError:
            title_t = i.find("div").find('a')
            book_title = title_t.get('title')
            book_url = title_t.get('href')

        # 如果網址為 javascript:void(0)，則跳過這筆資料
        if book_url == "javascript:void(0)":
            continue

        try:
            author_p = i.find("p", class_="author")
            authors = author_p.find_all("a")
            author_names = ", ".join([author.get_text(strip=True) for author in authors])
        except AttributeError as NoneTypeError:
            author_names = ""

        try:
            price_li = i.find("ul", class_="price").find("li")
            price_text = price_li.get_text(strip=True)
        except AttributeError as NoneTypeError:
            price_text = ""

        # 寫入 CSV 檔案
        writer.writerow({'書名': book_title, '網址': book_url, '作者': author_names, '書價': price_text})

