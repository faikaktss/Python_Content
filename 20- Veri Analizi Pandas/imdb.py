import pandas as pd
from pandas.io.sql import read_sql_query
df = pd.read_csv("imdb.csv",encoding="UTF-8")

# 1- Dosya hakkındaki bilgiler
result = df
result = df.columns
result = df.info

# 2- ilk 5 kaydı gösterin
result = df.head()

# 3- ilk 10 kaydı gösterin
result = df.head(10)

# 4- Son 5 kadı gösterin
result = df.tail()

# 5- Son 10 kaydı gösterin
result = df.tail(10)

# 6- Sadece Movie_Title kolonunu akın.
result = df["Title"]

# 7- Sadece Movie_Title kolonunu içeren ilk 5 kaydı alın
result = df["Title"].head()

# 8- Sadece Movie_Title  Rating kolonunu içeren ilk 5 kaydı alın
# result = df[["Title","Rating"]].head()

# 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın
# result = df[["Title","Rating"]].tail(7)

# 10- Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alın
# result = df[5:][["Title","Rating"]].head()

# 11- Sadece Movie_Title ve Rating kolonunu içeren ve imbd puani 
#     8.0 ve üstünde olan kayıtlardan ilk 50 tanesini alınız
result = df[df["Title"] >= '8']["Title"].head(50)

print(result)