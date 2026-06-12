# OOP:

# 1. Class :  student(self):
        # __init__(self):
        
        
        
        
# class paramveer:
#     def __init__(self, name):
#         self.name = name
        
#     def show(self):
#         print(self.name)
        
# p = paramveer("Paramveer")
# p.show()

# example 1

# class paramveer:
#     def __init__(self):
#         print("calling constructor")
        
#     def show(self):
#         print("Show the name")
        
# p = paramveer()
# p.show()


# example 2

# class paramveer:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def getAge(self):
#         print("My age is:",self.age)
        
#     def getName(self):
#         print("My name is:",self.name)
        
# # p = paramveer("Paramveer",20)
# # p.getName()
# # p.getAge()

# P = paramveer(age = 20, name = "Paramveer")
# P.getName()
# P.getAge()


# example 3

# class student:
#     def __init__(self, args):
#         print(type(args))
#         print(args)
#         self.name = args
        
#     def getStu(self):
#         #print("The student is:, ",self.name)
#         return self.name
        
# s = student({"name": "Paramveer", "age": 20})
# t = s.getStu()
# print(t["age"])



# example 4

class student:
    def __init__(self, *args):
        self.data = args
        
    def users(self):
        for i in self.data[0]:
            print(i)
    
    def details(self):
        print(self.data[1])
        for i in self.data[1]:
            print(i)
    
s = student({"dheeraj", "kunal", "harsh", "praveen"}, {"address": "kukas", "College": "arya", "location": "jaipur"})
s.users()
s.details()




# class student:
#     def __init__(self, **args):
#         self.data = args
        
    def data(self):
        print(self.data)
