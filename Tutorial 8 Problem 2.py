# Problem 2 - Create a function that returns an int, if possible
#
# Write a function that has a single argument. It tries to convert this argument to an integer.
#
# if it succeeds, it returns the integer
# if the conversion fails, it returns the original string
# e.g.
#
# print ( toInt('800') *3)  will print 2400
# print ( toInt('cat') *3)  will print 'catcatcat'
#
# Use the try-except construct to implement this.

def toInt(argument):
    try:
        argument = int(argument)
        return argument
    except:
        return argument

print (toInt(40.6)*3)


