# A statement is a part of the program which executes something
# A block is a group of consecutive statements that are at the same level in the structure of the program.
# age = int(input("Enter your age: "))
age = 10
if age > 17:
    # beginning of the conditional block
    print("You are of age!")
    age = age + 1
    print("You are now one year older...")
    # end of the conditional block

print("This here belongs to another block")
# NB: the main block of a Python program must always be at the leftmost edge of the file, without indentation:
# this program will not work because it is not written at the leftmost egde of the file
#   print("hello world")
#   print("this program is not very good...") --- gives IndentationError
# An expression is a bit of code that results in a determined data type.
# Because all expressions have a type, they can be assigned to variables:
# A function executes some functionality. Functions can also take one or more arguments, which are data that can be fed to and processed by the function
# A parameter is a variable in a function definition
# An argument is an actual value given in the function call.
# type function to find the data type of an object.
print(type("Harsh")) # O/P:- <class 'str'>
# SyntaxError :- If the syntatic rules are not followed.
# If the syntax of the program is correct but the program still doesn't function as intended, there is a bug in the program.
### Debugging
# 2 types of bug:-
# Generates error during execution:- Easy to fix as the line of the code is mentioned.
# Result of the code is wrong:- locating this type of bug is challenging.
#  Debugging is an extremely important skill in any programmer's toolbox. Professional programmers often spend more time debugging than writing fresh code.
# An effective way of debugging is adding debugging print statements to the code.
# Verifying the result of the code with print commands gives a quick confirmation the code does what it needs to do.
# Example


# hourly_wage = float(input("Hourly wage: "))
# hours = int(input("Hours worked: "))
# day = input("Day of the week: ")

# daily_wages = hourly_wage * hours
# if day == "sunday":
#     daily_wages * 2

# print(f"Daily wages: {daily_wages} euros")


# Above code does not work we have to fix it:-
# Debugging usually means running the program multiple times. 

# Step-1 :- Temporarily "Hard-Code" the problematic input
hourly_wage = 20
hours = 6
day = "sunday" #Fixed
daily_wages = hourly_wage * hours
# if day == "sunday":
#     daily_wages * 2

# print(f"Daily wages: {daily_wages} euros")
# Still obviously incorrect input

# Step-2 :- Add debugging print statements before and after the problematic part of code
# if day == "sunday":
#     print("wages_before ", daily_wages) #Debug1
#     daily_wages * 2
#     print("wages_after ", daily_wages) #Debug2
# print(f"Daily wages: {daily_wages} euros")
# Observation:- Running that prints nothing suggesting that if block is not getting executed at all
# Conclusion:- The problem is with conditional statement

# Step-3:- Add more debugging print statements 
# print("Condition: ", day == "sunday")
# if day == "sunday":
#     print("wages_before ", daily_wages) #Debug1
#     daily_wages * 2
#     print("wages_after ", daily_wages) #Debug2
# print(f"Daily wages: {daily_wages} euros")
# Observation:- Output gives false
# Conclusion:- The if statement never runs and the problem is indeed with conditional statement
# Analysis:- The input of day is "Sunday" whereas in conditional statement its "sunday" and that's the problem.
# After debugging remove the print statements and the hard-code part.

print("Condition: ", day == "sunday")
if day == "sunday":
    daily_wages * 2
print(f"Daily wages: {daily_wages} euros")

# Another example:- 
