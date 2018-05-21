#データをインポート
import json
import pandas as pd
with open("./2018/201803.txt", "r") as f:
    data = pd.DataFrame([json.loads(d, encoding = 'utf-8') for d in f.read().split('\n')[:] if len(d) > 0] )

#いらないカラムを削除
empty_columns = []
for column in data.columns:
    if not data[column].any():
        empty_columns.append(column)
data1 = data.drop(empty_columns, axis=1)

keywords = ["Solidity","Dapps","Crypto","cryptocurrency", "decentralize","ICO","暗号通貨",
            "スマートコントラクト"," Smart Contract","ハッシュパワー","分散型台帳","サトシナカモト",
            "サイドチェーン","Segwit", "ライトニングネットワーク","tokensale","トークンセール",
            "Tokenization","仮想通貨", "ビットコイン","BTC","ETH","Bitcoin", "Ethereum","イーサリアム",
            "Xem","XRP","Nem","Ripple","MONA","モナコイン","COSMA","ハードフォーク",
            "ビットコインキャッシュ","BCH","マイニング", "マウントゴックス","ホットウォレット",
            "コールドウォレット", "億り人", "草コイン", "アルトコイン", "Binance",
            "CoinCheck", "bitpoint"]

vocabularies = {}
for i in range(10): #とりあえず10まで
    author = data1.author_id[i].replace("twitter.com:", "")
    author_vocabulary = {}
    #for keyword in keywords:
        #author_vocabulary[keyword] = 0
    for keyword in keywords:
        if data1.body.str.contains(keyword)[i] == True and keyword not in author_vocabulary.keys():
            author_vocabulary[keyword] = 1
        if data1.body.str.contains(keyword)[i] == True:
            author_vocabulary[keyword] += 1
    vocabularies[author] = author_vocabulary

    print(author + " " + str(vocabularies[author]))
