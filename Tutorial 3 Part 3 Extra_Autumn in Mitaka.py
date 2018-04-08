# This program will draw a field of trees in autumn, it takes a while...about 2-3 minutes on my 2012 macbook pro
# make sure you are not running any other programs while you execute this program

"Autumn in Mitaka"

import turtle
import random

autumn = ["#8B4513","#A0522D","#A52A2A","#800000","#FFF8DC","#FFEBCD","#FFE4C4","#FFDEAD","#F5DEB3","#DEB887","#D2B48C","#BC8F8F","#F4A460","#DAA520","#CD853F","#D2691E"]



def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'X':
        newstr = 'F+[[X]-X]-F[-FX]+X'   # Rule 1
    elif ch == 'Y':
        newstr = 'F → FF'
    else:
        newstr = ch     # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    savePosition = []
    saveAngle = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.color(random.choice(autumn))
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            savePosition.append(aTurtle.pos())
            saveAngle.append(aTurtle.heading())
        elif cmd == ']':
            aTurtle.penup()
            restorePosition = savePosition.pop()
            restoreAngle = saveAngle.pop()
            aTurtle.setpos(restorePosition)
            aTurtle.setheading(restoreAngle)
            aTurtle.color(random.choice(autumn))
            aTurtle.pendown()

def main():
    inst = createLSystem(6, "X")  # create the string
    t = turtle.Turtle()           # create the turtle
    t.color("#FFF8DC")
    wn = turtle.Screen()
    wn.tracer(0)
    turtle.mode("logo")
    wn.bgcolor("#efccba")

    x = -350
    y = 270

    for i in range(10):
        t.up()
        t.setpos(x,y)
        t.down()
        drawLsystem(t, inst, 20, 5)   # draw the picture
        t.setheading(0)
        x += 80

    x = -340
    y = 170

    for i in range(7):
        t.up()
        t.setpos(x,y)
        t.down()
        drawLsystem(t, inst, 20, 10)   # draw the picture
        t.setheading(0)
        x += 150

    x = -250
    y = -50

    for i in range(4):
        t.up()
        t.setpos(x,y)
        t.down()
        drawLsystem(t, inst, 20, 20)   # draw the picture
        t.setheading(0)
        x += 200

    x = -300
    y = -380

    for i in range(4):
        t.up()
        t.setpos(x,y)
        t.down()
        drawLsystem(t, inst, 20, 30)   # draw the picture
        t.setheading(0)
        x += 250

    wn.exitonclick()

main()


