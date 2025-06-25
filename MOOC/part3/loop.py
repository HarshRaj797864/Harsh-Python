# When there are nested loops, break and continue commands only affect the innermost loop which they are a part of. 

number = int(input("Please type in a number: "))
while number > 0:
    i = 0
    while i < number:
        print(f"{i} ", end="")
        i += 1
    print()
    number -= 1

# Method important for sorting
number = int(input("Please type in a number: "))
 
left = 1
right = number
 
while left < right:
    print(left)
    print(right)
    left += 1
    right -= 1
 
if left == right:
    print(left)
