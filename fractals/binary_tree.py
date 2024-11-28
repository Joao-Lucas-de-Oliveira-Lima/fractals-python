import turtle

def configure_screen():
    screen = turtle.Screen()
    screen.setup(width=1200, height=600)
    screen.bgcolor("black")
    screen.title("Fractal - Binary Tree")
    return screen

def configure_turtle():
    t = turtle.Turtle()
    t.speed(0) 
    t.hideturtle()
    t.penup()
    t.goto(0, -300) 
    t.pendown()
    t.left(90) 
    return t

def calculate_color(depth):
    r = int((depth * 15) % 256)
    g = int((50 + depth * 20) % 256)
    b = int((100 + depth * 10) % 256)
    return (r, g, b)

def draw_binary_tree(t, branch_length, min_length, depth=0):

    if branch_length <= min_length:
        return

    t.color(calculate_color(depth))
    t.pensize(max(1, int(branch_length / 20)))

    t.forward(branch_length)

    t.left(45)
    draw_binary_tree(t, branch_length * 2 / 3, min_length, depth + 1)

    t.right(90)
    draw_binary_tree(t, branch_length * 2 / 3, min_length, depth + 1)

    t.left(45)
    t.backward(branch_length)

def main():
    turtle.colormode(255)
    screen = configure_screen()
    t = configure_turtle()
    draw_binary_tree(t, branch_length=200, min_length=10)
    turtle.done()

if __name__ == "__main__":
    main()
