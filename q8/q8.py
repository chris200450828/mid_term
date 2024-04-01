import requests
import q8_command_stuff as qcs
import pandas as pd

url = "https://www.googleapis.com/books/v1/volumes"
url_params = {'q': 'Python', 'maxResults': 10, 'projection': 'lite'}

r = requests.get(url, params=url_params)
data = r.json()
title, author, link, puber, pubDate = qcs.get_data(data, pop=False)

url_params['startIndex'] = 10

next_r = requests.get(url, params=url_params)
next_data = next_r.json()
n_title, n_authors, n_link, n_puber, n_pubDate = qcs.get_data(next_data, pop=False)

result_title = qcs.merge(title, n_title)
result_author = qcs.merge(author, n_authors)
result_link = qcs.merge(link, n_link)
result_puber = qcs.merge(puber, n_puber)
result_pubDate = qcs.merge(pubDate, n_pubDate)
result_data = zip(result_title, result_author, result_link, result_puber, result_pubDate)

encoding = 'utf-8'
df = pd.DataFrame(result_data, columns=['title', 'authors', 'URL', 'publisher', 'publishedDate'])
df.to_csv('pythonbook.csv', index=False, encoding=encoding)
