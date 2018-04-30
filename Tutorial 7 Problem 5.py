# There are two methods of handling files:
#
# using something like f=open(filename, 'r'), writing the file, then using an explicit f.close()
# using the with open(filename, 'r') as f: construct
#
# Whichever one you used for Problem 1, create an alternate version using the other method.

filename = input("Save to what file: ")
with open(filename, 'w') as f:
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
