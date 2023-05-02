import pandas as pd
df = pd.read_html("https://en.wikipedia.org/wiki/List_of_largest_fish")
df = pd.DataFrame(df[0])
df = df.drop(df.columns[[0, -1,-2]], axis=1)

df.iloc[:, 3] = df.iloc[:, 3].str.replace(r'\[(.*?)\]', '', regex=True)
df.iloc[:, 4] = df.iloc[:, 4].str.replace(r'[\[\(].*?[\]\)]', '', regex=True).str.replace(r'[^0-9.]', '', regex=True)
df.columns = df.columns.str.replace(r' \(.*?\)', '', regex=True)

df.to_csv('🐟.csv', index=False)