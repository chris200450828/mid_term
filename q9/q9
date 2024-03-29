import q9_command_stuff as cf
import pandas as pd
import os

cf.get_release()
cf.link_mix()
data = cf.get_release_data()


def file_exist_checker():
    file = "movie.csv"
    if os.path.isfile(file):
        print("File exist,process failed")
        return False
    else:
        return True


encoding = 'utf-8-sig'
if file_exist_checker():
    df = pd.DataFrame(data, columns=['Name', 'Release_Date', 'URL'])
    df.to_csv('movie.csv', index=False, encoding=encoding)
    print("process success")
