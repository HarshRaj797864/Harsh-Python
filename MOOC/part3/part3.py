# To create a loop you'll often need to include three distinct steps: initialisation, condition, and updating the iteration variables.
# Initialisation refers to setting the initial value(s) of the variable(s) used within the condition of the loop
# The condition defines for how long the loop is to be executed. It is set out at the very beginning of the loop.
# Finally, within each repetition of the loop the variables involved in the condition are updated
course = "Introduction to Programming"
grade = 4

verdict = "You have received "
verdict += f"the grade {grade} "
verdict += f"from the course {course}"

print(verdict)
