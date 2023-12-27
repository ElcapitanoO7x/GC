
# ############ Using Graphics Library ##############

# from graphics import *

# def circle_Bresenhams():
#     x = 0
#     r = int(input("Enter the circle radius: "))
#     y = r

#     p = 3 - 2*r
#     win = GraphWin("Bresenham's Circle circle Drawing Algorithm", 500, 500)

#     while x < y:
#         if p < 0:
#             x += 1
#             pt = Point(x, y)
#             pt.draw(win)
#             p = p + 4*x + 6
#         else:
#             x += 1
#             y -= 1
#             pt = Point(x, y)
#             pt.draw(win)
#             p = p + 4*(x - y) + 10


#     win.getKey()

# circle_Bresenhams()



############# Using Turtle Library ##############


from turtle import *
tracer(0)
speed(0)
hideturtle()
# colormode(0)

def cir(r):
    pu()
    x = 0
    y = r
    p = 3 - 2*r

    def all_octants():
        pu()
        goto(x, y)
        pd()
        dot()
        pu()
        goto(y, x)
        pd()
        dot()
        pu()
        goto(-y, x)
        pd()
        dot()
        pu()
        goto(-x, y)
        pd()
        dot()
        pu()
        goto(-x, -y)
        pd()
        dot()
        pu()
        goto(-y, -x)
        pd()
        dot()
        pu()
        goto(y, -x)
        pd()
        dot()
        pu()
        goto(x, -y)
        pd()
        dot()
        pu()

    while x < y:
        if p < 0:
            all_octants()
            x += 1
            p = p + 4*x + 6
        else:
            all_octants()
            x += 1
            y -= 1
            p = p + 4*(x-y) + 10
    pu()
    goto(0, -10)
    pu()
    write(arg="Mustafa Mohamad Barakat", move=True, align="center", font=("normal", 30, "bold"))
    done()

cir(300)