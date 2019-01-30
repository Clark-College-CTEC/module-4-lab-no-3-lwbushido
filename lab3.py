# Lab No. 3
# CTEC 121
# Lawrence Williamson

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)

    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    
    circle1 = Circle(Point(200,170), 50)
    circle1.setFill('white')
    circle1.draw(win)
    circle2 = Circle(Point(200,300), 80)
    circle2.setFill('white')
    circle2.draw(win)
    circle3 = Circle(Point(200,450), 100)
    circle3.setFill('white')
    circle3.draw(win)



    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2

    eye1 = Circle(Point(170,150), 10)
    eye1.setFill('red')
    eye1.draw(win)

    eye2 = Circle(Point(210,150), 10)
    eye2.setFill('red')
    eye2.draw(win)



    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose
    nose = Polygon(Point(195, 170), Point(200, 200), Point(210, 215))
    nose.setWidth(10)
    nose.setFill('orange')
    nose.draw(win)



    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat
    hat = Rectangle(Point(120, 120), Point(260, 120))
    hat.setWidth(10)
    hat.draw(win)
 

    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline
    hat1 = Line(Point(170, 50), Point(220, 50))
    hat1.draw(win)
    hat2 = Line(Point(170, 50), Point(170, 120))
    hat2.setWidth(60)
    hat2.draw(win)
    hat3 = Line(Point(225, 50), Point(225, 120))
    hat3.setWidth(60)
    hat3.draw(win)


    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()