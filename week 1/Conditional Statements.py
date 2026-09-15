age = int(input("Enter your age: "))
if age >= 18:
    print("you are adult")
else:
    print("you are a minor")
    
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")
    
positive = int(input("Enter a Number: "))
if positive > 0:
    print("positive")
elif positive <0:
    print("negative")
else:
    print("zero")
    
grade = int(input("Enter your grade"))
if grade > 90:
    print("Excellent")
elif grade >= 75:
    print("Passed")
else :
    print("Failed")