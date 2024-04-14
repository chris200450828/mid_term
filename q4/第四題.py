import requests
from bs4 import BeautifulSoup
import csv

requests.packages.urllib3.disable_warnings()

url = "https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv"
response = requests.get(url, verify=False)

with open("NHI_EnteroviralInfection.csv", 'w', encoding='utf-8-sig') as csvfile:
    csvfile.write(response.content.decode('utf-8-sig'))


print("CSV文件已成功写入。")
