# Problem 3 - Create a number-to-word converter for (1-9)
#
# Create a function that has one parameter - a number, and returns (but does NOT print) the textual version of that number.
#
# so print( toWord(9) ) displays nine
#
# There are multiple ways of doing this, using multiple if statements or a using a list, which is simpler.

def toWord(argument):
    dict = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    return dict[argument]

for num in range(1,10):
    print(toWord(num))
