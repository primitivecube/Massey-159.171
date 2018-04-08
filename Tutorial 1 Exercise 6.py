import math

#Volume of a sphere:
#Write instructions to compute the volume of a sphere with radius entered by the user.
#The formula for volume V: 𝑉𝑉=4𝜋𝜋3𝑟𝑟3.
#There is a predefined constant math.pi in Python.
#Testcase: a sphere with radius of 2m has a volume of ≈ 33.510 cubic metres.

r = int(input("Enter a radius: "))
v = ((4*math.pi)/3)*(r**3)
print("The volume of a sphere with a radius of {} is {}".format(r,v))

#Parallel Resistors:
#The combined resistance of three resistors connected in parallel is given by
#Combined resistance = 11𝑅𝑅1+1𝑅𝑅2+1𝑅𝑅3
#Write Python instructions to compute the combined resistance when the values
#for the three resistors are entered by the user.
#Testcase: three resistors of 5, 10, and 20 ohms in parallel should give a combined resistance of ≈ 2.85714 ohms.

r1 = int(input("Resistance for R1: "))
r2 = int(input("Resistance for R2: "))
r3 = int(input("Restistance for R3: "))
combined_resistance = 1 / ((1 / r1)+(1 / r2)+(1 / r3))
print("The combined resistance for resistors of {},{} and {} is {}".format(r1,r2,r3,combined_resistance))

#Temperature Converter:
#F = C * 9 / 5 + 32
#This converts temperatures from Centigrade to Fahrenheit.
#Test value: 20 degrees C convert to 68 degrees Fahrenheit

c = int(input("Enter a centigrade temperature: "))
f = (c * 9) / 5 + 32
print("{} degrees Centigrade is equal to {} degrees Fahrenheit".format(c,f))

# 3x2 – 5x + 10,
# when the value for x is entered by the user.
x = int(input("provide a value for x: "))
eqnA = (3 * x ** 2) - (5 * x) + 10
print("The equation (3x2 – 5x + 10) for an x value of {} evaluates to {}".format(x,eqnA))

#Eqn: c = 􀶥𝑥𝑥2+(−5)𝑦𝑦, when the user enters the values for x and y
#aution: for the values you enter, make sure that x2 is greater than -5y otherwise
#it'll try to find the square root of a negative number and math.sqrt() will give a Domain error.
#e.g. inputting 10 for x, and 5 for y will work as sqrt(100-25) is 8.66025,
#but entering the values the other way around means it will try to find sqrt(-75) which is a problem.

x = int(input("Input a value for x: "))
y = int(input("Input a value for y (must be lower than x): "))
c = math.sqrt((x ** 2) + ((-5) * y))
print("The equation (square root of (x pow 2 + -5 pow y)) for an x value of {} and a y value of {} evaluates to {}".format(x,y,c))
