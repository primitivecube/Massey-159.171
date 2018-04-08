# a) Write a program that prints ‘even’ and ‘odd’ one after another up to and including a user specified limit.
#     e.g. if the user enter a limit of 5 the output would be:
# Enter limit: 5
# odd
# even
# odd
# even
# odd
# hint: use the modulus % operator to work out even and odd numbered lines

count = 0
max = int(input("Enter a limit: "))
for i in range(1, max+1):
    if i % 2 == 1:
        print ("odd")
    else:
        print ("even")


# b) Break this program into a function where you can now pass the words that are printed and the limit as parameters:
# print_alternates( limit, word1, word2)
# e.g. print_alternates(4, ‘red’, ‘gold’) will output the following:
# red
# gold
# red
# gold

def print_alternates (limit, word1, word2):
    for i in range (1, limit+1):
        if i % 2 == 1:
            print(word1)
        else:
            print(word2)

print_alternates(4, 'red', 'gold')
