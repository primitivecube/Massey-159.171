# Use nested loops to print the following pairs of numbers:
# 0, 0
# 0, 1
# 0, 2
# 1, 0
# 1, 1
# 1, 2
# 2, 0
# 2, 1
# 2, 2
# Use the outer loop to generate the first number in the pair.
# Use the inner loop to generate the second number in the pair and print each pair.

for first in range (3):
    for second in range (3):
        print ("{}, {}".format(first, second))
