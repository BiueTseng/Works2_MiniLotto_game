import sqlite3
import random
import matplotlib.pyplot as plt
import numpy as np

#建立資料庫連線
conn = sqlite3.connect('analyze.db')
#建立鼠標
cursor = conn.cursor()
# #生成資料表
# # cmd = '''CREATE TABLE if not exists EX1 (ID integer primary key autoincrement,
# #         N1 int, N2 int, N3 int, N4 int, N5 int, N6 int);'''
# # cursor.execute(cmd)
# #
# # print('Table created')
# # #生成不重複亂數
# # for i in range(20):
# #     num = random.sample(range(1,21),6)
# #     print(num)
# #     #將資料寫入資料庫
# #     cmd = "INSERT INTO EX1 (N1, N2, N3, N4, N5, N6) values (?, ?, ?, ?, ?, ?)"
# #     cursor.execute(cmd,num)
# #     print('Data has been insert into database')
# 讀取資料庫
# cmd = "SELECT N1,N2,N3,N4,N5,N6 from Numdb"
# cursor.execute(cmd)
# data = []
# count = int()
#
#
# # print(len(cursor.fetchall()))
#
# for d in cursor.fetchall():
#     count += 1
#     print(d)
#     for i in d:
#         data.append(i)
#
# freq_data = []
# for i in sorted(set(data)):
#     freq_data.append(data.count(i)/len(data))
#     print(f'{i}:{data.count(i)}')
#
# print(count)
# print(freq_data)
# #關閉資料庫連線
# conn.commit()
# conn.close()
#

#畫直條圖
# plt.figure(figsize=(4.5, 5.8))
# plt.barh(range(1,21),freq_data,tick_label=range(1,21),color='#3e82fc')
# plt.xticks(np.arange(0,0.1,0.01))
# plt.axvline(x=0.05-2*pow((0.05*0.95/len(data)),0.5),c='#c74767',ls='--')
# plt.axvline(x=0.05+2*pow((0.05*0.95/len(data)),0.5),c='#c74767',ls='--')
# plt.title(f'Cumulative distribution of the {count}th number')
#
# plt.xlabel("Probability")
# plt.ylabel("Number")
# plt.show()
