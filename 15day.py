# Pandas frames methods:

# import pandas as pd

# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# # get single column data
# print(df["name"])
# # head -> starting 5 rows
# # print(df.head(-3))
# # tail -> ending 5 rows
# #print(df.tail(-3))
# # print(df.shape)

# #print(df.rename(columns = {"name": "student_name"}, inplace = True))

# print(df.describe())

# import pandas as pd

# data = {
#     "Emp_ID": [101, 102, 103, 104, 105, 106],
#     "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
#     "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
#     "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
#     "Experience": [2, 3, 5, 4, 1, 3]
# }

# df = pd.DataFrame(data)
# print(df.loc[4, "Emp_ID"])
# print(df.iloc[0:5])
# print(df.loc[0:"Name"])
# print(df.loc[5])

#print(df)

#print(df.head(5))
#print(df.tail(3))
#print(df.shape)
#print(df.info())
#print(df.info(verbose = True))
#print(df.info(verbose = False))
# df.rename(columns = {"Name": "Emp_name"}, inplace = True)
# print(df)
#print(df.describe())




# import pandas as pd

# d = {
#     "name": ["vishal", "virat", "vineet"],
#     "salary": [100, 200, 300]
# }

# df = pd.DataFrame(data = d)
# # add column
# df["marks"] = [10, 20, 30]
# df["marks"] = df["salary"] / 2
# df["increment"] = df["salary"] + (df["salary"] / 10)

# edit column name
# df.rename(columns = {"increment": "salary_increment"}, inplace = True)
# print(df)

# df["holiday"] = df["salary"] / 100
# df["decrement"] = [10, 20, 30]
# # delete column
# df.drop(["salary", "name"], axis = 1, inplace = True)
# print(df)

# print(df.loc[2, "name"])
# print(df.iloc[2, 0])
# print(df.iloc[1])
# print(df.loc[1])
# print(df.iloc[0:3])
# print(df.loc[0:3])
# df1 = df.iloc[0:2, [0]]#rows -> 0,1 & cols -> 0 | name
# print(df1)

# df2 = df.loc[0:2, ["name"]]


