# import pandas package

import pandas as pd
# # 1d -> method Serie

# example 1
# l = [10, 20, 30]
# df = pd.Series(data = l)
# print(df)


# example 2

# d = {"name": "kunal", "age": "21","roll-no": "123" }
# df = pd.Series(data = d, index = ["name", "age", "roll-no"])
# print(df)


# d = {
#     "name": ["Kunal", "Dheeraj", "Anjali", "Praveen", "Yash", "Danish"],
#     "roll-no": [12, 13, 14, 15, 16, 17]
# }

# df = pd.DataFrame(data = d)
# print(df)


url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
print(df)


