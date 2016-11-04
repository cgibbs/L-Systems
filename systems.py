# http://dcs.asu.edu/faculty/abansal/CST100/chap10/chap10_3.html

import turtle

def createLSystem(numIters,axiom):
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
    if ch == 'F':
        newstr = 'F-G++G-F'     # Rule 1
    elif ch == 'G':
        newstr = 'G+H-F-H+G'     # Rule 2
    elif ch == 'H':
        newstr = 'FFBBFF'            # Rule 3
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle,instructions,angle,distance):
    for cmd in instructions:
        if cmd == 'F' or cmd == 'G' or cmd == 'H':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '*':
            aTurtle.left(angle * 2)
        else:
            print('Error:', cmd, 'is an unknown command')

def main():
    inst = createLSystem(5,"F")   #create the string
    print(inst)
    t = turtle.Turtle()           #create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
#    drawLsystem(t,inst,60,5)      #draw the picture
                                  #angle 60, segment length 5
    drawLsystem(t,inst,75,5)
    wn.exitonclick()

main()