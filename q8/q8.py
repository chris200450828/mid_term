import requests
import q8_command_stuff as qcs
import pandas as pd

url = "https://www.googleapis.com/books/v1/volumes"
url_params = {'q': 'Python', 'maxResults': 10, 'projection': 'lite'}

r = requests.get(url, params=url_params)  #請求api
data = r.json()
title, author, link, puber, pubDate = qcs.get_data(data, pop=False)  #處理請求後的資料

url_params['startIndex'] = 10  #設定第二頁要用到的參數

next_r = requests.get(url, params=url_params)  #請求api
next_data = next_r.json()
n_title, n_authors, n_link, n_puber, n_pubDate = qcs.get_data(next_data, pop=False)  #處理請求後的資料

result_title = qcs.merge(title, n_title)  #混合函式發揮作用
result_author = qcs.merge(author, n_authors)
result_link = qcs.merge(link, n_link)
result_puber = qcs.merge(puber, n_puber)
result_pubDate = qcs.merge(pubDate, n_pubDate)
result_data = zip(result_title, result_author, result_link, result_puber, result_pubDate)

encoding = 'utf-8-sig'
df = pd.DataFrame(result_data, columns=['title', 'authors', 'URL', 'publisher', 'publishedDate'])
df.to_csv('pythonbook.csv', index=False, encoding=encoding)
