# By Brett McDonald
# SID: 10158931
# Tutorial 9
# Problem 1: Using a global variable as a counter

count = 0 # Initiate the count variable

def x():
  global count # prepare the global count variable for modification
  count += 1 # increment the global count variable
  print("Called {} times".format(count)) # display the number of times the function has been called

x()

x()

x()

# Result
# Called 1 times
# Called 2 times
# Called 3 times

