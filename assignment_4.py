# ----------------------------
# if statement
# ----------------------------

# 1. Check whether a person is eligible to vote.
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")

# 2. Check whether a number is positive.
num = int(input("Enter number: "))
if num > 0:
    print("Positive number")

# 3. Check whether a student scored more than 90 marks.
marks = int(input("Enter marks: "))
if marks > 90:
    print("Scored more than 90")

# 4. Check whether a product is in stock.
stock = int(input("Enter stock: "))
if stock > 0:
    print("Product is in stock")

# 5. Check whether user's age is greater than or equal to 18.
age = int(input("Enter age: "))
if age >= 18:
    print("User is 18 or above")

# 6. Check whether a temperature is above 100.
temp = float(input("Enter temperature: "))
if temp > 100:
    print("Temperature is above 100")

# 7. Check whether salary is greater than 50000.
salary = int(input("Enter salary: "))
if salary > 50000:
    print("Salary is greater than 50000")


# ----------------------------
# if - else statement
# ----------------------------

# 1. Positive or Negative
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
else:
    print("Negative")

# 2. Even or Odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Vote Eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible")

# 4. Pass or Fail
marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# 5. Balance Check
balance = int(input("Enter balance: "))
payment = int(input("Enter payment amount: "))
if balance >= payment:
    print("Payment Successful")
else:
    print("Insufficient Balance")

# 6. Product Stock
stock = int(input("Enter stock: "))
if stock > 0:
    print("Available")
else:
    print("Out of Stock")

# 7. Fever or Normal
temp = float(input("Enter temperature: "))
if temp >= 100:
    print("Fever")
else:
    print("Normal")


# ----------------------------
# if - elif - else
# ----------------------------

# 1. Grade Calculator
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")

# 2. Age Classification
age = int(input("Enter age: "))
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")

# 3. Traffic Signal
signal = input("Enter signal (red/yellow/green): ")
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")

# 4. Discount
amount = int(input("Enter purchase amount: "))
if amount >= 5000:
    print("30% Discount")
elif amount >= 3000:
    print("20% Discount")
elif amount >= 1000:
    print("10% Discount")
else:
    print("No Discount")

# 5. Temperature Classification
temp = float(input("Enter temperature: "))
if temp < 20:
    print("Cold")
elif temp < 30:
    print("Warm")
elif temp < 40:
    print("Hot")
else:
    print("Very Hot")

# 6. Membership
points = int(input("Enter membership points: "))
if points >= 1000:
    print("Platinum")
elif points >= 700:
    print("Gold")
elif points >= 400:
    print("Silver")
else:
    print("Regular")

# 7. Menu Driven Program
print("1. Hello")
print("2. Good Morning")
print("3. Thank You")
choice = int(input("Enter choice: "))
if choice == 1:
    print("Hello")
elif choice == 2:
    print("Good Morning")
elif choice == 3:
    print("Thank You")
else:
    print("Invalid Choice")


# ----------------------------
# Nested if
# ----------------------------

# 1. Exam Eligibility
attendance = int(input("Enter attendance percentage: "))
if attendance >= 75:
    fees = input("Fees paid? (yes/no): ")
    if fees == "yes":
        print("Eligible for Exam")
    else:
        print("Pay Fees")
else:
    print("Low Attendance")

# 2. Login System
username = input("Enter username: ")
if username == "admin":
    password = input("Enter password: ")
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

# 3. ATM
card = input("Card inserted? (yes/no): ")
if card == "yes":
    pin = int(input("Enter PIN: "))
    if pin == 1234:
        print("Access Granted")
    else:
        print("Wrong PIN")
else:
    print("Insert Card")

# 4. College Admission
marks = int(input("Enter marks: "))
if marks >= 60:
    documents = input("Documents verified? (yes/no): ")
    if documents == "yes":
        print("Admission Confirmed")
    else:
        print("Verify Documents")
else:
    print("Not Eligible")

# 5. Online Shopping
stock = input("Product available? (yes/no): ")
if stock == "yes":
    payment = input("Payment done? (yes/no): ")
    if payment == "yes":
        print("Order Confirmed")
    else:
        print("Complete Payment")
else:
    print("Product Out of Stock")

# 6. Hospital Appointment
registered = input("Patient registered? (yes/no): ")
if registered == "yes":
    doctor = input("Doctor available? (yes/no): ")
    if doctor == "yes":
        print("Appointment Confirmed")
    else:
        print("Doctor Not Available")
else:
    print("Please Register")