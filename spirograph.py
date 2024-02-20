import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pensize(3)
t.speed(15)
for i in range(6):
    for col in ("red", "magenta", "blue", "cyan", "green","yellow"):
        t.color(col)
        t.circle(150)

        t.left(10)
        t.hideturtle()

col = ('white', 'yellow','cyan')
for i in range(300):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)