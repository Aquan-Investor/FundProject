import os, sys
sys.path.append(os.pardir)
import json
import pandas as pd
with open("./FundProject/2018/201803.txt", "r") as f:
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
regex1 = r'RT @'
regex2 = r'@'
regex3 = r'http.+'
pattern1 = re.compile(regex1)
pattern2 = re.compile(regex2)
pattern3 = re.compile(regex3)
for i in range(len(data)):
    flag = False
    if data1.source_url[i] in target_client:
        flag = True
    if pattern1.match(data1.body[i]) != None:
        flag = False
    if pattern2.match(data1.body[i]) != None:
        flag = False
    if pattern3.match(data1.body[i]) != None:
        flag = False
    if flag:
        data2 = data2.append(data1.iloc[i])

data2.to_csv("test2.csv")
