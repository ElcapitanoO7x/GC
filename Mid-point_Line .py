# Mustafa Mohamad Barakat - CS

############# Using Graphics Library ##############


# from graphics import *

# def Line_Mid_Point_Algorithm():
#     x1 = int(input("Enter x1: "))
#     y1 = int(input("Enter y1: "))
#     x2 = int(input("Enter x2: "))
#     y2 = int(input("Enter y2: "))

#     x = x1
#     y = y1
#     dx = x2 - x1
#     dy = y2 - y1
#     d = dy - (dx/2)

#     win = GraphWin("Mid-point line drawing Algorithm", 500, 500)

#     while (x < x2):
#         pt = Point(x, y)
#         pt.draw(win)
#         x += 1

#         if (d < 0):
#             d = d + dy
#         else:
#             d = d + dy - dx
#             y += 1

#     win.getKey()

# Line_Mid_Point_Algorithm()



############# Using Turtle Library ##############


from turtle import *
tracer(0)
speed(0)
hideturtle()
pensize(0.1)

def Bresenhams_Algorithm(x1, y1, x2, y2):
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    d = dy - (dx/2)

    def plot():
        pu()
        goto(x, y)
        pd()
        dot()
        pu()

    while x < x2:
        if d < 0:
            plot()
            x += 1
            d = d + dy
        else:
            plot()
            x += 1
            y += 1
            d = d + dy - dx

    done()


Bresenhams_Algorithm(0, 0, 100, 100)