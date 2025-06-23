print("Hello, World!")
# print has many functionalities like ","
result = 10 * 25
# print("The result is " + result) #generates TypeError
print("The result is", result) # a whitespace is automatically added
# easily printing multiple datatypes with f-strings
name = "Mark"
age = 37
city = "Palo Alto"
print(f"Hi {name}, you are {age} years old. You live in {city}.")
# Another tedious way is using "," operator but we have to take care of extra white space.
# floating point numbers = decimal numbers
print("Hi!", end=" ") #If you don't want print statement to end in a new line
print("There")

# note: input always takes input from user as string datatype
# therefore to input numbers from user type-casting is needed
year = int(input("Enter the year: "))
print(f"Your age at the end of 2025 is {2025-year}")
# Another example
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

height = height / 100
bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi}")
# Try to limit the use of variables
# Don't try to use same variable name for different data types makes it more confusing
print(int(3.6))
# Indentation in python is key do not forget it
# Boolean values : True and False
print(2 < 5 & 3)
# we can import pre-defined functions from modules 
# a common module is math
from math import sqrt
print(sqrt(9))


