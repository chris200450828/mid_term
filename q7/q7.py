import pandas as pd

import q7_command_stuff as qcs

result_list = []
TEAM = ["CLE", "HOU", "GSW"]
team_name_l, num_l, name_l, pos_l, ht_l, wt_l, exp_l, college_l, birth_l = [], [], [], [], [], [], [], [], []

#    呼叫鏈結混合函式
url = qcs.start_up(TEAM)
for i in url:
    print(i)
    soup = qcs.get_soup(i)
    qcs.get_data(soup)
    result_list.append(qcs.get_data(soup))

#    重新壓縮zip
for i in result_list:
    for j in i:
        obj = list(j)
        print(obj)
        num_l.append(obj[0])
        name_l.append(obj[1])
        pos_l.append(obj[2])
        ht_l.append(obj[3])
        wt_l.append(obj[4])
        exp_l.append(obj[5])
        college_l.append(obj[6])
        birth_l.append(obj[7])
        team_name_l.append(obj[8])

result = zip(num_l, name_l, pos_l, wt_l, exp_l, college_l, birth_l, team_name_l)

encodings = 'utf-8-sig'
df = pd.DataFrame(result,
                  columns=['No.', 'Name', 'Position', 'Weight', 'Experience', 'College', 'Birth', 'Team'])
df.to_csv('player.csv', index=False, encoding=encodings)
