import pandas as pd
from pandas.core.frame import DataFrame

# df = pd.read_csv('sample.csv')
# df = pd.read_jaon('sample.json',encoding="UTF-8") 
# df = pd.read_excel("sample.xlsx")

connection = sqlite3.connet("sample.db")
df = pd.read_sql_query("SELECT * FROM students", connection)

print(df)