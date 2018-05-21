import os, sys
sys.path.append(os.pardir)
import json
import pandas as pd
with open("test.txt", "r") as f:
    data = pd.DataFrame([json.loads(d, encoding = 'UTF-8') for d in f.read().split('\n')[:] if len(d) > 0] )

for i in len(data):
    print(data.body[i])
    print("---------------------------")
    print()
