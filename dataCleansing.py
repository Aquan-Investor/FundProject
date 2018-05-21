#データをインポート
import os, sys
sys.path.append(os.pardir)
import json
import pandas as pd
with open("./2018/201803.txt", "r") as f:
    data = pd.DataFrame([json.loads(d, encoding = 'UTF-8') for d in f.read().split('\n')[:] if len(d) > 0] )

#いらないカラムを削除
empty_columns = []
for column in data.columns:
    if not data[column].any():
        empty_columns.append(column)
data1 = data.drop(empty_columns, axis=1)

#クライアントを抽出
data2 = pd.DataFrame(columns = data1.columns)
target_client = ["Twitter for iPhone", "Twitter for Android", "Twitter Web Client"]


import re
regex = r'RT @'
pattern = re.compile(regex)
for i in range(len(data1.body)):
    flag = False
    if data1.source_url[i] in target_client:
        flag = True
    if pattern.match(data1.body[i]) != None:
        flag = False
    if flag:
        data2 = data2.append(data1.iloc[i])

print(data2)
