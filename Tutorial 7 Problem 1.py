# Problem 1 - Save your input lines to a file
#
# Write a function that asks for a filename, and then repeatedly reads lines from the user and saves these lines to the named file.
#
# It stops saving the lines when the user input is a single dot on a line by itself. The line containing the single dot is NOT saved.
#
# e.g. a run of your program might look something like this:
#
# Save to what file: mytest.txt
# > This is
# > my attempt at
# > Tut 7, problem 1
# >
# > the last line was empty
# > .
# Saving file mytest.txt
# 5 lines saved
# If you open the file in PyCharm or Notepad, it would contain:
#
# This is
# my attempt at
# Tut 7, problem 1
#
# the last line was empty
# You can open the newly created file in PyCharm to check its contents.

filename = input("Save to what file: ")
f = open(filename, 'w')
line_count = 0
while True:
    line = input('> ')
    if line == '.':
        print('Saving file {}'.format(filename))
        print('{} lines saved'.format(line_count))
        break
    else:
        f.write(line+'\n')
        line_count += 1
f.close()
