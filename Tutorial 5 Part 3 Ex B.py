# Create a big box out of n rows of little o's for any desired size n.'
# Use an input statement to allow the user to enter the value for n and then print the properly sized box.
# E.g. n = 3
# oooooo # n*2 symbols in top row
# o    o # n number of rows. One symbol at each edge of each row between top and bottom. There are n-2 middle rows.
# oooooo # n*2 symbols in bottom row

# let's get the first row working...

# n = 3
# for i in range (n*2):
#     print("o", end = "")
# print()

# let's manually enter the middle row/s...

# for i in range (n-2):
#     space = " "
#     print("{0}{1}{0}".format("o", space * (n*2-2)))
# print()

# Now to combine them into a function...

def boxOfSymbols ():
    rows = int(input("Enter the number of rows: "))
    symbol = str(input("Enter a symbol as the box boundary: "))
    for i in range (rows*2):
        print(symbol, end = "")
    print()
    for i in range (rows-2):
        space = " "
        print("{0}{1}{0}".format(symbol, space * (rows*2-2)), end = "")
        print()
    for i in range (rows*2): # yes, I've repeated myself, but writing another function for this piece seems unnecessary
        print(symbol, end = "")

boxOfSymbols()
