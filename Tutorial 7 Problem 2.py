# Problem 2 - Copying a file
#
# Write a function copyFile() that has two string parameters - these are both filenames.
#
# the first parameter is the name of an existing file
# the second is the name of a new file.
# Read the contents of the first file and write these lines into a file with the second filename.
#
#
# IMPORTANT: You can use PyCharm to create tiny text files to use as test files. If you do this, create a text file
# (i.e. choose File NOT Python File when adding a file to the project)
# otherwise PyCharm will insist on error checking the file for valid Python.

def copyFile(existing_file, new_file):
    a = open(existing_file, 'r')
    b = open(new_file, 'w')
    list = a.readlines()
    b.writelines(list)
    a.close()
    b.close()

copyFile('movies.txt', 'moviesthe2nd.txt')

