# HW 9.1 - Application of Turtle_Drawing.py
import turtle
from TurtleDrawings_classPolygon import *
#---------------------
if __name__ == "__main__":
    turtle.setup(800, 800)
    turtle.title("HW9.1 Application of user-defined module TurtleDrawings with class Polygon")
    t = turtle.Turtle()
    t.shape("classic")
    fin = open("polygon_drawings.txt", 'r')
    L_drawings = fget_drawings(fin)
    fin.close()
    for polygon in L_drawings:
        print(polygon)
        polygon.turtle_draw(t)