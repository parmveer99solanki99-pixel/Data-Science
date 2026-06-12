# num1 = 10
# num2 = 20
# print(num1 and num2)

# num1 = "Hello"
# num2 = ""
# print(num1 or num2)

# a = 5  # 101
# b = 2  # 010
# print(a & b) # bitwise AND


# Identity operator: is, is not

# name = "Hello"
# print(name is "Hello")
# print(name == "Hello")

# num1 = 268
# num2 = 268

# print(num1 == num2)
# print(num1 is num2)
# print(id(num1))
# print(id(num2))



# Conditional Statement: 
# 1. if 
# 2. elif
# 3. else

# num1 = 10
# num2 = 20

# if num1 < num2:
#     print(num2)
    
# if else statement

# num1 = int(input("Enter the number: "))
# if num1:
#     print("number:", num1)
# else:
#     print("Zero", num1)
    
    

# # if elif else statement

# age = int(input("Enter the age: "))
# if age == 18:
#     print("Your age is: ", age)
# elif age > 18:
#     print("You are above than ", age)
# else:
#     print("You are less than ", age)


# marks = int(input("Enter the marks: "))

# if marks > 90:
#     print("Grade: A")
# elif marks >= 75 and marks <= 90:
#     print("Grade: B")
# elif marks >= 60 and marks < 75:
#     print("Grade: C")
# else:
#     print("Fail")



# Loops:

# for loop

# L = [11, 12, 13, 14]
# print(len(L))

# for i in range(len(L)):
#     print(L[i])
#     i += 1



l = [10, [11, 12, 13, 14]]

for i in range(len(l)):
    print(i)
    l[1][i]

# 1. ATM Withdrawal System

balance = 10000

while True:
    amount = int(input("Enter withdrawal amount: "))

    if amount == 0:
        break

    if amount <= balance:
        balance -= amount
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")


# 2. Student Result Analyzer

passed = 0
failed = 0

for i in range(1, 6):
    marks = int(input(f"Enter marks of student {i}: "))

    if marks >= 40:
        print("Pass")
        passed += 1
    else:
        print("Fail")
        failed += 1

print("Total Passed:", passed)
print("Total Failed:", failed)


# 3. Password Retry System

password = "python123"
attempts = 0

while attempts < 3:
    user = input("Enter password: ")

    if user == password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")

    attempts += 1

if attempts == 3:
    print("Account Locked")


# 4. Electricity Bill Calculator

for i in range(1, 4):
    units = int(input(f"Enter units for customer {i}: "))

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    print("Bill Amount:", bill)


# 5. Number Guessing Game

secret = 25
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print("Correct Guess")
        print("Attempts:", attempts)
        break
