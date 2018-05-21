import os, sys
sys.path.append(os.pardir)
import json 
import pandas as pd
with open("./2017/201710.txt", "r") as f:
    data = pd.DataFrame([json.loads(d,encoding = 'UTF-8') for d in  f.read().split('\n')[:] if len(d) > 0] )
empty_columns = []
for column in data.columns:
   if not data[column].any():
       empty_columns.append(column)
data1 = data.drop(empty_columns, axis=1)
data_clientCleanse = pd.DataFrame(columns = data1.columns)
target_client = ["Twitter for iPhone", "Twitter for Android", "Twitter Web Client"]

for i in range(len(data1)):
   if data1.source_url[i] in target_client:
       data_clientCleanse = data_clientCleanse.append(data1.iloc[i])

#print(data_clientCleanse)
users=data_clientCleanse.author_id
dic={}
for user in users:
    if user in dic.keys():
         dic[user]+=1
    else:
        dic[user]=1
users=set(data_clientCleanse.author_id)
for user in users:
    if dic[user]<15:
        dic.pop(user)
keywords = ["ビットコイン",
"BTC",
"ETH",
"Bitcoin",
"Ethereum",
"イーサリアム",
"Nem",
"Xem",
"XRP",
"Ripple",
"MONA",
"モナコイン",
"COMSA",
"ハードフォーク",
"ビットコインキャッシュ",
"BCH",
"マイニング",
"マウントゴックス",
"ホットウォレット",
"コールドウォレット",
"ICO",
"億り人",
"草コイン",
"仮想通貨",
"暗号通貨",
"アルトコイン",
"Binance",
"CoinCheck",
"bitpoint",
"Solidity",
"Dapps",
"Crypto",
"cryptocurrency",
"decentralize",
"スマートコントラクト",
"Smart Contract",
"ハッシュパワー",
"bitcoiner",
"分散型台帳",
"サトシナカモト",
"サイドチェーン",
"Segwit",
"ライトニングネットワーク",
"ブロックチェーン",
"tokensale",
"トークンセール",
"Tokenization"]
users=dic.keys()
key_count_by_user={}
for user in users:
    key_count_by_user[user]={}  #初期化
    rows=data_clientCleanse[data_clientCleanse.author_id==user]
    print(user)
    for word in keywords:
        #print(word)
        for index,row in rows[rows.body.str.contains(word)].iterrows():
            if word in key_count_by_user[user].keys():
                key_count_by_user[user][word]+=1
            else:
                 key_count_by_user[user][word]=1

print(key_count_by_user)
