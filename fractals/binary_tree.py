import turtle

def configure_turtle():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Fractal - Árvore Binária")
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(0, -300) 
    t.pendown()
    t.left(90)
    return t

def make_binary_tree(t, size, limit, depth=0):

    if size <= limit:
        return
    
    r = int((depth * 15) % 256)
    g = int((50 + depth * 20) % 256)
    b = int((100 + depth * 10) % 256)
    t.color((r, g, b))
    
    t.pensize(max(1, int(size / 20)))
    
    t.forward(size)
    
    t.left(45)
    make_binary_tree(t, size * 2 / 3, limit, depth + 1)
    
    t.right(90)
    make_binary_tree(t, size * 2 / 3, limit, depth + 1)

    t.left(45)
    t.backward(size)

turtle.colormode(255)
screen = turtle.Screen()
screen.setup(width=1200, height=600)
t = configure_turtle()
make_binary_tree(t, size=200, limit=10)
turtle.done()
