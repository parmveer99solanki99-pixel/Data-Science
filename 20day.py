# import matplotlib.pyplot as plt

# x = [2010, 2015, 2020, 2025]
# y = [100, 200, 250, 300]

# plt.figure(figsize = (5, 5))
# plt.plot(x, y)
# plt.xlabel("years")
# plt.ylabel("sales")
# plt.title("Sales Report")
# plt.show()


# import matplotlib.pyplot as plt

# x = [2010, 2015, 2020, 2025]    # x cord
# y1 = [100, 200, 260, 290]        # y cord
# y2 = [150, 185, 195, 300]

# # plt.figure(figsize = (4, 3))  # width  or height
# plt.plot(x, y1, label = "jeans")  # Line graph
# plt.plot(x, y2, label = "shirt")
# plt.legend()  # info of label
# plt.show()      # graph show


# plt.plot(x, y, color = 'red', marker = 'o',
#          linestyle = 'dashed',
#                     linewidth = 4, markersize = 14)

# plt.plot(x, y)  # Line graph
# plt.show()      # graph show 


# import matplotlib.pyplot as plt

# x = [2010, 2013, 2016, 2019]

# y1 = [15000, 21700, 22600, 20199]
# y2 = [750500, 890050, 1059000, 79800]

# plt.figure(figsize = (4, 2))
# plt.plot(x, y1, label = "Total_Sale")
# plt.plot(x, y2, label = "Total_Profit")
# plt.legend()
# plt.show()



# bar chart
# import matplotlib.pyplot as plt
# x = [2015,2020,2025,2030]
# y = [100,150,200,290]

# plt.bar(x,y)
# # size
# plt.figure(figsize=(6,2))
# plt.show()


# multi ba chart

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])

y1 = [10, 20, 20, 40]
y2 = [20, 30, 25, 30]

# calculation -> width

w = 0.40
plt.bar(x - w/2, y1, label = "boys", width = w)
plt.bar(x + w/2, y2, label = "girls", width = w)

plt.xlabel("groups")
plt.ylabel("number of students")
plt.title("Number of students in Each group")
plt.legend()
plt.show()
