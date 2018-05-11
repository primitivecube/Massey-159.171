
# Problem 1: Using Try-Except so number input handles errors
#
# Write a function called getNumber(prompt, whichType) that can be used to input numeric values, so instead of using
#
# height = float(input("How tall are you: '))
#
# you'd use your function:
#
# height = getNumber("How tall are you: ", 'float')
#
# Importantly, your function should handles cases where the input cannot be converted to a number
#
# normally entering 'hi' when a number is wanted would cause your program to die
# instead, use the try - except construct to trap the error and let the user try again
# The routine should continually prompt until a number satisfying whichType is entered by the user.
#
# The parameters are:
#
# prompt - what to display as part of the input()
# whichType - this is a string and contains either integer or float, and indicates the type of result wanted.
# it might be used like this
#
# amount = getNumber("How much is the item: ", 'float')
# howMany= getNumber("How many do you want: ", 'integer')
# ...
# There's a simpler version of getNumber() that you can use as a model in the lecture notes on Exceptions.
#
# The general form of a try-except block is:
#
# try:
#     some statements
#     that might fail
# except:
#     what to do
#     if they fail


def getNumber(prompt, whichType):
    if whichType == 'float':
        while True:
            try:
                reply = input(prompt)
                value = float(reply)
                return value
            except:
                print ("Invalid number, try again")
    elif whichType == 'integer':
        while True:
            try:
                reply = input(prompt)
                value = int(reply)
                return value
            except:
                print ("Invalid number, try again")

amount = getNumber("How much is the item: ", 'float')
howMany = getNumber("How many do you want: ", 'integer')


