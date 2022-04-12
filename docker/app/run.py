import pandas as pd

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'

df = pd.read_csv(url)

df["nova_coluna"] = 'teste'

print(df.columns)

print(df.head())

print(df.shape)
