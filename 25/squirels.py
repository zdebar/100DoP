import pandas

data = pandas.read_csv("25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].value_counts()
df = fur_color.reset_index().rename(columns={'index': 'Index', 'Primary Fur Color': 'Fur Color', 'count': 'Count'})
print(type(df))
print(df)