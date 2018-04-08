# Print the following for any positive integer n.
# Use an input statement to allow the user to enter the value for n and
# then print the properly sized box.
# Don't worry about handling the spacing for multi-digit numbers.
# E.g. n = 3
# 1 3 5 5 3 1 # There are n*2 variables in a row, and n*2 columns. The top and bottom rows have n numbers.
# 3 5     5 3 # The second row has n*2-2 numbers
# 5         5 # The third row has n*2-4 numbers
# 5         5 # spaces commence after reaching the highest number in a sequence
# 3 5     5 3
# 1 3 5 5 3 1
# E.g. n = 5
# 1 3 5 7 9 9 7 5 3 1
# 3 5 7 9     9 7 5 3 # 5 spaces = row * 4 + 1
# 5 7 9         9 7 5 # 9 spaces = row * 4 + 1
# 7 9             9 7 # 13 spaces = row * 4 + 1
# 9                 9
# 9                 9
# 7 9             9 7
# 5 7 9         9 7 5
# 3 5 7 9     9 7 5 3
# 1 3 5 7 9 9 7 5 3 1

# Let's print just the top row...

# n = 3

# sequence = 1
# for i in range (0,n-1):
#     print (sequence, " ", end = "")
#     sequence += 2
# print (sequence, " ", end = "")
# for i in range (n,n*2-1):
#     print (sequence, " ", end = "")
#     sequence -= 2
# print (sequence, " ", end = "")

# It's messy, but it works. Now to make it a box...
# n = 3
# sequence = 1
#
# for a in range(n*2):
#     for i in range (0,n-1):
#         print (sequence, " ", end = "")
#         sequence += 2
#     print (sequence, " ", end = "")
#     for i in range (n,n*2-1):
#         print (sequence, " ", end = "")
#         sequence -= 2
#     print (sequence, " ", end = "")
#     print()

# The box is working, but I'm not happy with this whole approach. Maybe indexing is the way forward...

# n = 3
# list = []
# number = 1
# rowNumber = 0
# for i in range (n):
#     list.append(number)
#     number += 2
# print (list)

# Now we have all the numbers we need for indexing...

# for b in range (0,n):
#     print(list[b], " ", end = "")
# for c in range (n-0):
#     print(list[~c], " ", end = "") # the ~ symbol is a special trick for reverse indexing :)
# print ()
# rowNumber += 1
#
# # Looking good, what does the next row look like?
#
# for b in range (1,n):
#     print(list[b], " ", end = "")
#     if list[b] == max(list):
#         space = " "
#         print (space * rowNumber * n*2, end = "") # the space calculation doesn't work for all values, I'll fix it later...
# for c in range (n-1):
#     print(list[~c], " ", end = "")
# print ()
# rowNumber += 1
#
# # And now the middle rows...
#
# for b in range (2,n):
#     print(list[b], " ", end = "")
#     if list[b] == max(list):
#         space = " "
#         print (space * rowNumber * n*2, end = "")
# for c in range (n-2):
#     print(list[~c], " ", end = "")
# print ()

# Okay, now to manually complete the box...
#
# for b in range (2,n):
#     print(list[b], " ", end = "")
#     if list[b] == max(list):
#         space = " "
#         print (space * rowNumber * n*2, end = "")
# for c in range (n-2):
#     print(list[~c], " ", end = "")
# print ()
# rowNumber -= 1
#
# for b in range (1,n):
#     print(list[b], " ", end = "")
#     if list[b] == max(list):
#         space = " "
#         print (space * rowNumber * n*2, end = "")
# for c in range (n-1):
#     print(list[~c], " ", end = "")
# print ()
# rowNumber -= 1
#
# for b in range (0,n):
#     print(list[b], " ", end = "")
# for c in range (n-0):
#     print(list[~c], " ", end = "")
# print ()

# Let's get automating...

# n = 4
#
# list = []
# number = 1
# rowNumber = 0
# rangeModifier = 0
#
# for i in range (n):
#     list.append(number)
#     number += 2
# print (list)
#
# def printSequence(i):
#
#     for b in range (i,n):
#
#         print(list[b], " ", end = "")
#
#         if list[b] == max(list):
#             space = " "
#             print (space * i * 6, end = "") # solved space calc through trial and error, not entirely sure why it works
#
#     for c in range (n-i):
#
#         print(list[~c], " ", end = "")
#
#     print()
#
# for z in range (n):
#     printSequence(z)
#
# for x in range (n-1,-1,-1):
#     printSequence(x)

# Finally, let's make it a tidy program with good variable naming:

def diamondBox():

    n = int(input("Enter an even number of rows: ")) // 2

    list = []
    number = 1

    for i in range (n):
        list.append(number)
        number += 2

    for topHalf in range (n):

        for index in range (topHalf,n):

            print(list[index], " ", end = "")

            if list[index] == max(list):
                space = " "
                print (space * topHalf * 6, end = "")

        for reverseIndex in range (n-topHalf):

            print(list[~reverseIndex], " ", end = "")

        print()

    for bottomHalf in range (n-1,-1,-1):
        for index in range (bottomHalf,n):

            print(list[index], " ", end = "")

            if list[index] == max(list):
                space = " "
                print (space * bottomHalf * 6, end = "")

        for reverseIndex in range (n-bottomHalf):

            print(list[~reverseIndex], " ", end = "")

        print()

diamondBox()

#Finished! Well that was difficult. Maybe there is a nested loop approach to this?
