import time
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Analog Clock")
wn.tracer(0)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(h, m, s, pen):
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)
    hands = [("white", 80, 12), ("blue", 150, 60), ("red", 110, 60)]
    time_set = (h, m, s)
    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)
        pen.rt(angle)
        pen.pendown()
        pen.fd(hand[1])


while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    draw_clock(h, m, s, pen)
    wn.update()
    time.sleep(1)
    pen.clear()
wn.mainloop()
