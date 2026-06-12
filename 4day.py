# Functions: 

# def hello():
#     print("hello function is working")
    
# hello()

# example 

# def add(a = 2, b = 1):
#     print(a, b)

# add(10, 5)

# add()

# Example 2

# def power(a,b):
#     print(a**b)
    
# power(5, 2)
# power(2,5)
# power(b = 5, a = 2)
# power(a =2, b = 5)

# Example 3

# def student(*a):
#     print(a)
#     print(type(a))
#     print(a[0])
    
# student(1, 2, 3, 4, 5, 6)

# question

def marks(*a): # parameter
    # for loop
    print(marks) # function name
    
marks(10, 20, 30, 40, 50)


# question

# def address(a):
#     # loop
#     for i in a:
#         for j in i:
#             print(j)
    
# address(["hello", "yourname"])

# output:
# h
# e
# l
# l
# o


# Lambda function

# add = lambda x: x
# print(add(100))

# sum = lambda x, y: x + y
# print(sum(10, 20))

# a = lambda x: [i for i in x]
# print(a([10, 20, 30, 40]))


# question

# a = lambda x: [i for i in x]
# print(a([10, 20, 30]))


# list comprehension [expression for item in iterable if condition]

# print([i for i in range(5)])

# example

# l = [10, 20, 30, 40, 50]
# print([i for i in range(len(l))])
# print([l]) 



# List

# L = [10, 20, 30]
# print(L[0])
# print(L[1])
# print(L[2])
# print(len(L))

# example of append
# L = ["hello", "yourname", "python"]
# L.append('for arya mains')
# print(L)
# print(L[0])
# print(L[-1])

#e example of insert

# L = [True, False, 10, 20]
# L.insert(1, 100)
# print(L)

# question

# l = [10, 20, 30, {"name": "yourname", "address": ["jaipur", "kukas", "home town", "friend house"]}]
# print(l[3]["address"])

# for i in l[3]["address"]:
#     print(i)

# question

# l = [10, 20, 30, [40, 50, [60, 70, 80] ]]
# for i in range(len(l[3])-1):
#     print(l[3][i])
    
# for i in l[3]:
#     print(i)


# d = {"name": "Hello"}
# print(d["name"])
# print(d.keys())
# print(d.values())


# d = {"name": "Hello", "age": 20}
# print(d.keys())
# print(d.values())

# for i in d.keys():
#     print("key: ", i)
#     print("value: ", d[i])

# Question

d = {
  "Message": "Number of Post office(s) found: 6",
  "Status": "Success",
  "PostOffice": [
    {
      "Name": "Achrol",
      "Description": "",
      "BranchType": "Sub Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Jaitpura Khinchi",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Kali Pahadi",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Kant",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Labana",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    },
    {
      "Name": "Rajpurawas Tala",
      "Description": "",
      "BranchType": "Branch Post Office",
      "DeliveryStatus": "Delivery",
      "Taluk": "Jaipur",
      "Circle": "Jaipur",
      "District": "Jaipur",
      "Division": "Jaipur Moffusil",
      "Region": "Jaipur HQ",
      "State": "Rajasthan",
      "Country": "India"
    }
  ]
}
for i in range(len(d["PostOffice"])):
    print(d["PostOffice"][i])
