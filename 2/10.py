import pandas as pd
# headerなし設定が必要
df = pd.read_csv('popular-names.txt', header=None)
print(len(df))
