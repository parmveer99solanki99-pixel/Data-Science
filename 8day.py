# Class

# class Address:
#     city = 'Jaipur'
#     state = "Rajasthan"
    
# a = Address()
# print(a.state)








# Constructor

# class Address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state

# a = Address("Jaipur", "Rajasthan")
# print(a.state)
# print(a.city)



# class Address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
        
#     def show(self):
#         print("The city is:", self.city)
#         print("The state is:", self.state)
        
# a = Address("Jaipur", "Rajasthan")
# a.show()



# Inheritance

# class Address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
        
#     def location(self):
#         return f"My location is {self.city} in {self.state}"
    
# class User(Address):
#     def __init__(self, name, age, city, state):
#             self.name = name
#             self.age = age
#             super().__init__(city, state)
            
#     def UserName(self):
#             print("My name is:", self.name) 
            
#     def userDetails(self):
#             print(f"My name is {self.name} and I am {self.age} years old.")
#             print(f"My location is {self.city} in {self.state}")
               
# u = User("Paramveer", 20, "Kukas", "Rajasthan")
# u.userDetails()

#a = Address("Kukas", "Rajasthan")
# print(u.location())




# Encapsulation

# class Address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
        
#     def location(self):
#         print(f"My location is {self.city} in {self.state}")
    
# a = Address("Chittorgarh", "Rajasthan")
# a.location()
# print(a.city)
# print(a.state)


# Polymorphism


# class Address:
    
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
        
#     def location(self):
#         print(f"My location is {self.city} in {self.state}")
        
        
# class HomeTown:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
        
#     def location(self):
#         print(f"My HomeTown is {self.city} in {self.state}")
        
        
# a = Address("Kukas", "Rajasthan")
# a.location()
# a = HomeTown("Chittorgarh", "Rajasthan")
# a.location()



# Class variable

# class Address:
#     total = 0
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#         Address.total += 1
        
#     def location(self):
#         print("location")
        
# a = Address("jaipur", "Rajasthan")

# b = Address("Chittorgarh", "Rajasthan")

# a.total

# print(a.total)


# Overloading --> not possible













# Overriding

# class Address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
        
#     def location(self):
#         print("address")
        
# class User(Address):
#     def __init__(self, name, age, city, state):
#         super().__init__(city, state)
#         self.name = name
#         self.age = age
        
#     def location(self):
#         print("user location")
        
# u = User("arya mains", 25, "Jaipur", "Rajasthan")
# a = Address("Chittorgarh", "Rajasthan")
# u.location()
# a.location()



# Tuple : immutable

# t = (10, 20, 30)
# print(t[0])
# print(t[-1])


# example

marks = [80, 90, 85, 98]

# list --> changeable

# marks[3] = 50
# print(type(marks))
# print(marks)

# tuple --> unchangeable

t = tuple(marks)
print(type(t))
print(t)
