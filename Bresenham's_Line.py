# Mustafa Barakat - CS

############# Using Graphics Library ##############


# from graphics import *

# def Bresenhams_Algorithm():
#     x1 = int(input("Enter x1: "))
#     y1 = int(input("Enter y1: "))
#     x2 = int(input("Enter x2: "))
#     y2 = int(input("Enter y2: "))

#     x = x1
#     y = y1
#     dx = x2 - x1
#     dy = y2 - y1

#     p = 2 * dy - dx

#     win = GraphWin("Bresenham's Line Drawing Algorithm", 500, 500)
    
#     while x <= x2:
#         pt = Point(x, y)
#         pt.draw(win)
#         x += 1

#         if p < 0:
#             p = p + 2 * dy
#         else:
#             p = p + 2 * dy - 2 * dx
#             y += 1
            
#     win.getKey()

# Bresenhams_Algorithm()

############# Using Turtle Library ##############


from turtle import *
tracer(0)
speed(0)
hideturtle()
pensize(0)

def Bresenhams_Algorithm(x1, y1, x2, y2):
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    p = 2*dy - dx

    def plot():
        pu()
        goto(x, y)
        pd()
        dot()
        pu()

    while x < x2:
        if p < 0:
            plot()
            x += 1
            p = p + 2*dy
        else:
            plot()
            x += 1
            y += 1
            p = p + 2*dy - 2*dx

    done()
# Bresenhams_Algorithm(0,0,100,100)
def Bresenhams_Algorithm(x1,y1,x2,y2):
    x=x1
    y=y1
    dx=x2 - x1
    dy=y2 - y1
    p=2*dy-dx

    def plot():
        pu()
        goto(x,y)
        pendown()
        dot()
        pu()
    while x<x2:
        if p<0:
            plot()
            x+=1
            p=p+2*dy
        else:
            plot()
            x+=1
            y+=1
            p=p+2*dy-2*dx
    done()
Bresenhams_Algorithm(0,0,100,100)