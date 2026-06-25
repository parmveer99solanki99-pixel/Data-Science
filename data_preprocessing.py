# import pandas as pd

# data = {
#     "Name": ["Ram", "Kamal", "Ajay"],
#     "Age": [20, None, 32],
#     "Salary": [5000, 6000, None]
# }

# df = pd.DataFrame(data)

# print("Original DataFrame")
# print(df)

# # 1. Find Null Values

# print("Null Values")
# print(df.isnull())

# print(df.isnull().sum())

# # 2. Fill Null Values


# # Fill Age with average Age
# df["Age"] = df["Age"].fillna(df["Age"].mean())

# # Fill Salary with average Salary
# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# print("DataGrame After Fillna()")
# print(df["Age"])

# # 3. Drop Null Values

# df_drop = df.dropna()

# print("DataFrame After dropna():")
# print(df_drop)


# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# data = {
#     'Name': ['Ram', 'Kamal', 'Ajay', 'Neetu', 'Kavi', 'Sapu'],
#     'Age': [25, None, 32, 20, 21, 22],
#     'Salary': [5000, 6000, None, 7000, 8000, 9000],
#     'Gender': ['male', 'male', 'male', None, 'female', 'female']
# }  

# df = pd.DataFrame(data)
# print("Original dataframe")
# print(df)

# # label encoding
# le = LabelEncoder()
# df_label = df.copy()
# df_label['Gender'] = df['Gender'].fillna('unknown')
# df_label['Gender_encoder'] = le.fit_transform(df_label['Gender'])

# print("After label Encoding")
# print(df_label)


# one hot encoding

# import pandas as pd

# data = {
#     'colors': ['red', 'blue', 'green', 'Red', 'Blue',]
# }

# df = pd.DataFrame(data)
# print("original data")
# print(df)

# df['colors'] = df['colors'].str.lower()
# # one hot encoding
# encode_df = pd.get_dummies(df, columns = ['colors'])

# print("After one hot encoding")
# print(encode_df)




# day 2

# handle missing values

# import pandas as pd
# import numpy as np

# data = {
#     "colors": ['red', 'green', 'blue', 'orange', 'green', 'blue', np.nan]
# } 

# df = pd.DataFrame(data)
# # print(df)

# # handle null values
# df.dropna(inplace = True)
# print(df)


# label encoding
# from sklearn.preprocessing import LabelEncoder

# le = LabelEncoder()
# df['colors_encoder'from django.conf import settings] = le.fit_transform(df['colors'])

# method 2
# df['colors_encoder2'] = LabelEncoder().fit_transform(df['colors'])

# method 3

# import sklearn
# df['colors_encoder3'] = sklearn.preprocessing.LabelEncoder().fit_transform(df['colors'])
# print(df)



# one hot encoding

# from sklearn.preprocessing import OneHotEncoder
# # print(df)

# # drop cols of label encoding

# if 'color_encoder' in df.keys():
#     df.drop(df[['colors_encoder', 'colors_encoder1', 'colors_encoder2', 'colors_encoding3']], axis = 1, inplace = True)
    
# print(df)

# # one hot encoding (by the help of pandas)

# df_encoder = pd.get_dummies(df, columns = ['colors'])
# print(df_encoder)




# combination of handle missing value | label encoding | one hot encoding

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data = {
    "age": [18, 20, np.nan, 26, 30],
    'gender': ['male', 'female', 'others', 'male', None],
    "name": ['dheeraj', 'kavi', 'sapu', 'yash', 'hello']
}

df = pd.DataFrame(data)

# handle missing values

df['age'] = df['age'].fillna(df['age'].mean())
df.dropna(subset = ['gender'], inpace = True)
print(df)

# label encoding

le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
print(df)



