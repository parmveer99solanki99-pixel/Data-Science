import pandas as pd

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
# by default ascending
# print(df.sort_values("english"))

# descending

# df.sort_values("english", ascending = False, inplace = True)
# print(df)


# by default ascending method 1

# df.sort_values(by = ["english"], inplace = True)
# print(df)

# descending
# df.sort_values(by = ["english"], ascending = False, inplace = True)
# print(df)

# df["name"] = df["name"].str.lower()
# df.sort_values("name", inplace = True)
# print(df)



import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df['doj'] = ['2025-01-10', '2025-02-10', '2025-03-10', '2025-04-10', '2025-05-10']
df['doj'] = pd.to_datetime(df['doj'])
print(df['doj'].dtype)
print(df['doj'].dt.year)
print(df['doj'].dt.month)
print(df['doj'].dt.day)
print(df['doj'].dt.day_name())
