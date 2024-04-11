import pandas as pd
import q7_command_stuff as qcs

result_list = []
TEAM = ["CLE", "HOU", "GSW"]
num_l, name_l, pos_l, ht_l, wt_l, exp_l, college_l, birth_l = [], [], [], [], [], [], [], []

url = qcs.start_up(TEAM)
for i in url:
    print(i)
    soup = qcs.get_soup(i)
    qcs.get_data(soup)
    result_list.append(qcs.get_data(soup))

#    解壓縮重新封裝zip
for i in result_list:
    for j in i:
        obj = list(j)
        num_l.append(obj[0])
        name_l.append(obj[1])
        pos_l.append(obj[2])
        ht_l.append(obj[3])
        wt_l.append(obj[4])
        exp_l.append(obj[5])
        college_l.append(obj[6])
        birth_l.append(obj[7])


result = zip(num_l, name_l, pos_l, ht_l, wt_l, exp_l, college_l, birth_l)

encodings = 'utf-8-sig'
df = pd.DataFrame(result, columns=['No.', 'Name', 'Position', 'Height', 'Weight', 'Experience', 'College', 'Birth'])
df.to_csv('player.csv', index=False, encoding=encodings)
