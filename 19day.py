# import pandas as pd
# import numpy as np

# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# df["marks"] = df["marks"].astype(object)
# df.loc[df["name"] == "anjali", "marks"] = 'Null'
# df.isnull()
# print(df.isnull().sum())

# print(df.dropna())   # drop null values  by row
# print(df.dropna(axis = 1))  #drop null values by col

# fill by zero
# print(df.fillna(0))

# fill by 100
# print(df.fillna(100))

# roll no -> 200 | marks -> 100

# print(df.fillna({"roll no": 200, "marks": 100}, inplace = True))

# marks -> mean | nan fill with average
# print(df.fillna({"marks": df["marks"].mean()}))


# aggregation
# # Manually
# print(df["marks"].sum())
# print(df["marks"].mean())
# print(df["marks"].min())
# print(df["marks"].max())

# Aggregation
# print(df["marks"].agg(["sum", "mean", "min", "max"] ))


# Concatenate


# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# df1 = pd.read_json(url)

# print(pd.concat([df, df1], axis = 1).fillna(df1["name": "paramveer"]))



