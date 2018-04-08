# a) Write a Python program that will print the following:
# 10
# 11 12
# 13 14 15
# 16 17 18 19
# 20 21 22 23 24
# 25 26 27 28 29 30
# 31 32 33 34 35 36 37
# 38 39 40 41 42 43 44 45
# 46 47 48 49 50 51 52 53 54
# Generate the output using nested for loops.
# Create a separate variable to store numbers that will be printed.
# Use end = " " in your print statement to print each row of numbers on the same line.

# This looks too hard, lets simplify the pattern:

# 1
# 2 3

# If I can solve this, I can solve the above problem. Let's think through it in natural language...

# print 1 number
# print 2 numbers

# let's substitute that for formal language...

# print(1)
# print(2,3)

# let's try manually writing a program that will create the desired pattern...

# for a in range (1, 2):
#     print (a, end = " ")
# print()
# for a in range (2,4):
#     print (a, end = " ")
# print()
# for a in range (4,7):
#     print (a, end = " ")
# print()
# for a in range (7, 11):
#     print (a, end = " ")
# print()

# The pattern is looking good, and it is clear that the range start and limit are the only variables
# that need to change each time. Let's figure out the pattern by which they change...

# x = 1
# y = 2
#
# for a in range (x, y): # 1, 2
#     print (a, end = " ")
# print()
#
# x += 1
# y += 2
#
# for a in range (x,y): # 2, 4
#     print (a, end = " ")
# print()
#
# x += 2
# y += 3
#
# for a in range (x,y): # 4, 7
#     print (a, end = " ")
# print()
#
# x += 3
# y += 4
#
# for a in range (x, y): # 7, 11
#     print (a, end = " ")
# print()

# Okay, so we need to initiate x at the start value, and y at the limit value, and then we need to increment the amount
# added to x and y by 1 after each time that addition is executed. Let's try that...

# x = 1
# y = 2
# changex = 0
# changey = 1
# for i in range (5):
#         # print (x, y)
#         for a in range (x, y):
#             print (a, end = " ")
#         changex += 1
#         changey += 1
#         x += changex
#         y += changey
#         print ()

# Great, the pattern is working. Now let's substitute the values to solve the initial problem,
# give proper variable names, and make it a function...

def number_stairs():
    start = int(input("Enter a starting number: "))
    steps = int(input("Enter the number of steps in the number stairs: "))
    limit = start+1
    incrementStart = 0
    incrementLimit = 1
    for step in range (steps):
            for num in range (start, limit):
                print (num, end = " ")
            incrementStart += 1
            incrementLimit += 1
            start += incrementStart
            limit += incrementLimit
            print () # to add a new line for each row

number_stairs()

# Excellent, job done :)
