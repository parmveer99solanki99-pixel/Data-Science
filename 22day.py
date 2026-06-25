# subplot

# import matplotlib.pyplot as plt

# # graph one data

# year = [2010, 2015, 2020, 2025]
# dairy = [100, 520, 630, 400]

# # graph two data

# year = [1990, 2000, 2005, 2010]
# farming = [300, 200, 250, 100]

# fig, aux = plt.subplots(1, 2, figsize = (6, 3))

# aux[0].plot(year, dairy, marker = 'o') # first col for line chart
# aux[0].set_xlabel("year")
# aux[0].set_ylabel("dairy")
# aux[0].set_title("dairy production graph")


# # this is second graph
# aux[1].plot(year, farming, marker = 'o') # first col for line chart
# aux[1].set_xlabel("year")
# aux[1].set_ylabel("farming")
# aux[1].set_title("farming production graph")

# plt.tight_layout()
# plt.show()





# import matplotlib.pyplot as plt

# students = ["A", "B", "C", "D", "E"]
# marks = [85, 90, 75, 88, 95]

# attendance = [80, 90, 75, 85, 95]

# ages = [18, 19, 18, 20, 19]

# fig, ax = plt.subplots(2, 2)

# # Line Chart
# ax[0,0].plot(students,marks,marker='o')
# ax[0,0].set_title("Marks Trend")
# ax[0,0].set_xlabel("Students")
# ax[0,0].set_ylabel("Marks")
# ax[0,0].grid(True)

# # Bar Chart
# ax[0,1].bar(students,attendance,color="orange")
# ax[0,1].set_title("Attendance")
# ax[0,1].set_xlabel("Students")
# ax[0,1].set_ylabel("Attendance %")

# # pie char
# ax[1,0].pie(ages,labels= students)

# # Histogram
# ax[1,1].hist(marks,bins=5,color="green",edgecolor="black")
# ax[1,1].set_title("Marks Distribution")
# ax[1,1].set_xlabel("Marks")
# ax[1,1].set_ylabel("Frequency")

# plt.tight_layout()

# #plt.gcf().canvas.get_supported_filestypes()
# plt.savefig("subplot1.pdf")

# plt.show()





# import pandas as pd
# import matplotlib.pyplot as plt
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-arya/main/temperature_data.json"
# df = pd.read_json(url)
# # print(df)



# # drop row 3 -> day = wednesday
# df.dropna(subset=["temperature_c"],inplace=True)
# #print(df)

# # fill average value -> humidity -> nan
# df.fillna(df['humidity_pct'].mean(),inplace=True)
# #print(df)

# # new cols -> farenheit | cell*1.8 -> + 32
# df['temperature_f'] = (df['temperature_c'] * 1.8)+32
# print(df)
# # subplots -> 1d -> line chart | pie chart
# fig,aux = plt.subplots(1,2)
# aux[0].plot(df["humidity_pct"],df["temperature_c"], marker = 'o')
# aux[0].set_xlabel("humidity")
# aux[0].set_ylabel("temperature in celsius")
# aux[0].set_title("humidity with celsius")

# aux[1].pie(df["temperature_f"],labels=df["day"],autopct="%1.1f%%")
# aux[1].set_title("humidity with farenheit")

# # save image data
# plt.show()



# Today Task: Create a Ecommerce project using numpy + pandas + matplotlib.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load JSON data
data =  "https://raw.githubusercontent.com/parmveer99solanki99-pixel/Data-Science/main/ecommerce.json"
df = pd.read_json(data)

print("Original Data")
print(df)

# Create Total Amount column
df["total_amount"] = df["price"] * df["quantity"]

print("Data with Total Amount")
print(df)

# NumPy Analysis

sales = np.array(df["total_amount"])

print("NumPy Analysis")
print("Total Revenue:", np.sum(sales))
print("Average Sale:", np.mean(sales))
print("Maximum Sale:", np.max(sales))
print("Minimum Sale:", np.min(sales))

# Product-wise Sales

product_sales = df("product")["total_amount"].sum()

print("Product-wise Sales")
print(product_sales)

# Category-wise Sales


category_sales = df("category")["total_amount"].sum()

print("Category-wise Sales")
print(category_sales)

# City-wise Sales


city_sales = df("city")["total_amount"].sum()

print("City-wise Sales")
print(city_sales)

# Date Analysis


df["order_date"] = pd.to_datetime(df["order_date"])

daily_sales = df("order_date")["total_amount"].sum()

print("\nDaily Sales")
print(daily_sales)

# Visualization 1
# Product-wise Revenue


plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Product Wise Revenue")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

# Visualization 2
# Category-wise Revenue


plt.figure(figsize=(6,6))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Wise Revenue")
plt.ylabel("")
plt.show()

# Visualization 3
# Daily Sales Trend


plt.figure(figsize=(8,5))
daily_sales.plot(kind="line", marker="o")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")

plt.show()

# Top Selling Product

top_product = product_sales.idxmax()
top_revenue = product_sales.max()

print("\nTop Selling Product")
print("Product:", top_product)
print("Revenue:", top_revenue)
