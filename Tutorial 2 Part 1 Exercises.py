def total (a, b, c):
    sum = a+b+c
    return sum

t1 = total(2,3,4) + total(4,6,8)
print(t1)

def blah():
    x = 2015
    print(x)

x = 234
print(x)

def banner(name):
    print("**************")
    print("           " + name)
    print("**************")

def block(x):
    x = x + 3

x = 5.6
block(x)
print(x)

def func(s):
    s = s * 2
    return s

food = 'bread'
func(food)
print(food)
print(func(food))

def fromDouble(x):
    print('fromDouble', x)
    return x*3

def subtract(y,z):
    print('from subtract', y, 'fromDouble', z)
    return y - z

result = subtract(20, fromDouble(10))
print(result)

price = 50
gst = price * 15.0 / 100
print("The price is ", price, " and the gst is ", gst)


num1 = input("enter number of tickets: ")
num2 = input("enter cost of tickets: ")
num1_int = int(num1)
num2_int = int(num2)
print("the total cost is", num1_int*num2_int)



def gst(num):
    gst = num * 15 / 100
    return gst

print(gst(200))

def totalGST(list):
    totalGST = 0
    for i in list:
        totalGST += gst(i)
    return totalGST

list = [100,200,300]

print(totalGST(list)) # should be 15 + 30 + 45 = 90

def gst(num):
    return num * 0.15

def totalGST(a,b,c):
    return gst(a) + gst(b) + gst(c)

print (totalGST(100,200,300))

print(gst(200))
