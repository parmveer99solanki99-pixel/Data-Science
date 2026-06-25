# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1, 2, 3, 4])
# y1 = [10, 20, 20, 40]
# y2 = [20, 30, 25, 30]
# y3 = [30, 40, 35, 20]

# w = 0.25
# plt.bar(x-w, y1, width=w, label = "boys")
# plt.bar(x, y2, width=w, label = "girls")
# plt.bar(x+w, y3, width=w, label = "Others")


# plt.xlabel("Groups")
# plt.ylabel("Number of students")
# plt.title("Number of students in Each group")
# plt.legend()
# plt.show()


#Histogram
# import matplotlib.pyplot as plt

# marks = [ 40, 55, 60, 70, 75, 90, 33, 50]
# plt.figure(figsize = (3,3))
# plt.hist(marks, bins = 3)
# plt.show() 



# Piechart

# import matplotlib.pyplot as plt
# fruits = ['apple', 'banana', 'orange', 'watermelon']
# count = [40, 30, 15, 70]
# plt.pie(count, labels = fruits, startangle = 90, autopct = '%1.1f%%')
# plt.axis('equal')
# plt.show()


# Subpolts

import matplotlib.pyplot as plt

# first chart

x = ['apple', 'banana', 'orange', 'watermelon']
y = [40, 30, 15, 70]
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 30, 40, 55]

plt.figure(figsize=(7, 6))

plt.subplot(2, 2, 1)
plt.plot(x, y, marker = 'o')
plt.xlabel("Fruits")
plt.ylabel("Count")
plt.title("Line Chart")

# second chart

plt.subplot(2, 2, 2)
plt.pie(y, labels = x, startangle = 90, autopct = "%1.1f%%")
plt.title("Fruit Distribution")


# third chart

plt.subplot(2, 2, 4)
plt.hist(y, bins = 4)
plt.title("Histogram")
plt.xlabel("Count")
plt.ylabel("Frequency")


# fourth

plt.subplot(2, 2, 3)
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("Fruits")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

