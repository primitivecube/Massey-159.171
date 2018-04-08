count = 0
total = 0
while count < 10:
    count += 1
    total += count**3
    if count == 3:
        continue
    print(count, "\t\t", count**3)
print("Total:\t\t{0}".format(total))
