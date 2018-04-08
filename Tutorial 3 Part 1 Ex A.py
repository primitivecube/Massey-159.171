# Display the following using the range() function and a for-loop
# i) the table for numbers from 1 to 10; with a total at the end of all the cubes
# ii) the table for values from 0 to 100 in steps of 10, with a total at the end of all the cubes
# Your program should display the number then its cube (the number multiplied by itself three times e.g. 33 = 27).

def cube_range(a,b,c):
    cube_sum = 0
    for i in range(a,b,c):
        print(str(i)+"\t\t"+str(i ** 3))
        cube_sum += i ** 3
    print("Total: \t"+str(cube_sum))

cube_range(1,11,1)
print()
cube_range(0,101,10)
