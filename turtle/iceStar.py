import turtle

t = turtle
t.Turtle()

def iceStar(size, limit):
    if(size < limit):
        return
    else:
        t.forward(size)
        t.color("blue")
        iceStar(size/3, limit)    
        t.right(72)
        iceStar(size/3, limit)
        t.right(72)
        iceStar(size/3, limit)
        t.right(72)
        iceStar(size/3, limit)
        t.right(72)
        iceStar(size/3, limit)
        t.right(72)
        iceStar(size/3, limit)
        t.left(360)
        t.backward(size)
        t.color("cyan")


t.speed(-10)
t.goto(0, 600)
t.bgcolor("black")
t.shape("classic")
t.right(90)

t.hideturtle()
iceStar(600, 20)

t.done()