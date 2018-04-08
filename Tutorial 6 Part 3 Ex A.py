# Exercise A: Coin toss generator
# a) Write a function coin_toss() which returns ‘heads’ or ‘tails’.
# To do this use random.randint() to generate a 0 or 1.
# Instead of 0 and 1 return heads or tails. Do this using if/else statements.
#  Don’t forget to import the random module!
# b) Now call the function coin_toss() a user specified number of times and print the results.
# For example if the user enters 5 then the output might look like this:
# number of coin tosses: 5
# heads
# tails
# heads
# heads
# tails
# Your output will always be different as it is dependent on the random numbers that are generated for the coin toss.
# c) Finally calculate a running total for the number of heads flipped, and the number of tails so that you final output might look like this:
# number of coin tosses: 5
# heads
# tails
# heads
# heads
# tails
# 3 x heads; 2 x tails

import random

def coin_toss():
    conditionA = random.randint(0,1) == 1
    if conditionA:
        return 'heads'
    else:
        return 'tails'

numberOfCoinTosses = int(input("Enter a whole number of coin tosses: "))
print("number of coin tosses: {}".format(numberOfCoinTosses))
headsCount = 0
tailsCount = 0

for i in range (numberOfCoinTosses):
    result = coin_toss()
    if result == 'heads':
        headsCount += 1
        print('heads')
    else:
        tailsCount += 1
        print('tails')

print(headsCount, "x heads;", tailsCount, "x tails")

