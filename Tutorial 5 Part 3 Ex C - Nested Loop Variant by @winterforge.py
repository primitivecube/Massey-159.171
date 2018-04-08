### This program was written by winterforge; it supported a pull request by primitivecube. Thanks winterforge! ###

# First thing is to initialise all of the counter variables
n = int(input("enter an integer: "))
n = n*2
a=1


# The for loops are split into two structures.
# One set creates the top half of the pattern, with the second set creating the bottom

for x in range (1,n,2):          # First level determines the rows. Begin at 1, count to 2 * n in increments of 2

    for y in range (a,n,2):      # Second loop prints the first half of each row
        print(y,end=" ")

    print(2*(a-1)*" ",end="")    # This line places the spaces that will make up the centre diamond into the string

    for y in range (n-1,a-1,-2): # Third loop creates the second half of the row by counting backwards
        print(y,end=" ")

    a +=2       # incrementing a here means the next row will begin with a number two larger than the previous row
    print()     # ends the current string and creates a new line



a -=2           # a must be decreased by one step before beginning the next loop or we end up with higher numbers



for x in range (1,n,2):          # This loop determines the rows of the second half. Same as above

    for y in range (a,n,2):      # this loop prints the first half of each row, but reverse of top half as a is counting back down to 1
        print(y,end=" ")

    print(2*(a-1)*" ",end="")     # places the white space as above

    for y in range (n-1,a-1,-2):  # again, reverse of top half as a is counting down instead of up
        print(y,end=" ")

    a -=2      # decrement a
    print()
