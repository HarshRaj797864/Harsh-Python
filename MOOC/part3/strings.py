# The * operator can also be used with a string, when the other operand is an integer.
# The string operand is then repeated the number of times specified by the integer.
word = "banana"
print(word*3)
# printing pyramid
n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1

# Underlining a string
# input_string = input("Please type in a string: ")
input_string = "Hello!"
print(input_string)
print("-"*len(input_string))

print("lalalalal", end="")
print("halal")


# Substring

input_string = "test"

print("t" in input_string)
print("x" in input_string)
print("es" in input_string)
print("ets" in input_string)

# find() --- returns position

input_string = "testis"

print(input_string.find("t"))
print(input_string.find("x"))
print(input_string.find("es"))
print(input_string.find("ets"))
print(input_string.find("is"))

# Note:- find is a method not a function.
# Methods work quite similarly to the functions covered in the previous part. What distinguishes them from functions is that methods are always attached to the object they are called on.

