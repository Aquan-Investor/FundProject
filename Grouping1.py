import os, sys
sys.path.append(os.pardir)
import json
import pandas as pd
with open("./2018/201803.txt", "r") as f:
    data = pd.DataFrame([json.loads(d, encoding = 'UTF-8') for d in f.read().split('\n')[:] if len(d) > 0] )

keywords = sorted(["Solidity","Dapps","Crypto","cryptocurrency", "decentralize","ICO","暗号通貨",
            "スマートコントラクト"," Smart Contract","ハッシュパワー","分散型台帳","サトシナカモト",
            "サイドチェーン","Segwit", "ライトニングネットワーク","tokensale","トークンセール",
            "Tokenization","仮想通貨", "ビットコイン","BTC","ETH","Bitcoin", "Ethereum","イーサリアム",
            "Xem","XRP","Nem","Ripple","MONA","モナコイン","COSMA","ハードフォーク",
            "ビットコインキャッシュ","BCH","マイニング", "マウントゴックス","ホットウォレット",
            "コールドウォレット", "億り人", "草コイン", "アルトコイン", "Binance",
            "CoinCheck", "bitpoint"])

# 値が入っていないカラムを削除
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

df1 = pd.DataFrame(index = keywords)
user_dict = {}

for i in range(1000): #どうやらlen(data1.body)くらいの大きさだと時間がかかるらしい
    counts = [0 for i in range(len(keywords))]
    for j in range(len(keywords)):
        if keywords[j] in data_clientCleanse.body[i]:
            counts[j] += 1
    sum_count = sum(counts)
    counts = pd.Series(counts, index = keywords)
    if data_clientCleanse.author_id[i] in list(df1.columns):
        df1[data_clientCleanse.author_id[i]] += counts
        user_dict[data_clientCleanse.author_id[i]] += sum_count
    else:
        df1[data_clientCleanse.author_id[i]] = counts
        user_dict[data_clientCleanse.author_id[i]] = sum_count
#print(df1)
user_dict = dict(sorted(user_dict.items(), key=lambda x: x[1]))
for key in user_dict.keys():
    print(key + "  " + str(user_dict[key]))
