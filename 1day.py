# Variable:- container to store values through memory space occupation.
a = 10
print(a)
print(id(a))
print(type(a))

# same values of two different variables will have same id because of memory optimization by python.
a = 10
b = 10
print(id(a))
print(id(b))

a = int(input("Enter  the number: "))
print(a)
print(type(a))
