# Mustafa Mohamad Barakat - CS


############# Using Graphics Library ##############


# from graphics import *
# def circle_Midpoint():
#     x = 0
#     r = int(input("Enter the circle radius: "))
#     y = r

#     p = 1 - r
#     win = GraphWin("Mid-point Circle Drawing Algorithm", 500, 500)

#     while x < y:
#         if p < 0:
#             x += 1
#             pt = Point(x, y)
#             pt.draw(win)
#             p = p + 2*x + 1
#         else:
#             x += 1
#             y -= 1
#             pt = Point(x, y)
#             pt.draw(win)
#             p = p + 2*x + 1 - 2*y  


#     win.getKey()

# circle_Midpoint()



############# Using Turtle Library ##############


from turtle import *
tracer(0)
speed(0)
hideturtle()

def cir(r):
    x = 0
    y = r
    p = 1 - r

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
            p = p + 2*x + 1
        else:
            all_octants()
            x += 1
            y -= 1
            p = p + 2*x + 1 - 2*y
    pu()
    goto(0, -10)
    pu()
    write(arg="Mustafa Mohamad Barakat", move=True, align="center", font=("normal", 30, "bold"))
    done()

cir(300)