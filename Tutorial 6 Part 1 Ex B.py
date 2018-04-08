# Write a program that will ask the user for seven numbers,
# print the total sum of the numbers and print the count of the positive entries,
# the number entries equal to zero, and the number of negative entries.
# Use a for loop and an if, elif, else chain, not just three if statements.
# Here is some sample output:
# Enter a number: -3
# Enter a number: -8
# Enter a number: 20
# Enter a number: 34
# Enter a number: 0
# Enter a number: -10
# Enter a number: 0
# Sum: 33
# Positives: 2, Negatives: 3, Zeros: 2

list = []
positiveEntries = 0
negativeEntries = 0
zeroEntries = 0
sumEntries = 0
for i in range (7):
    list.append(int(input("Enter a number: ")))
for j in list:
    sumEntries += j
    if j > 0:
        positiveEntries += 1
    elif j < 0:
        negativeEntries += 1
    else:
        zeroEntries += 1
print("Sum: {}\nPositives: {}, Negatives: {}, Zeros: {}".format(sumEntries, positiveEntries, negativeEntries, zeroEntries))

