import turtle

def configure_turtle():
    screen = turtle.Screen()
    screen.setup(width=1200, height=600)
    screen.bgcolor("black")
    screen.title("Fractal - Nested Squares")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.width(10)
    t.left(90)
    return t

def calculate_color(side_length, initial_side_length):
    intensity = max(0.4, side_length / initial_side_length)
    return (intensity, 0.1, 0.1)

def draw_nested_squares(t, side_length, divisor, base_case, initial_side_length):
    if side_length < base_case:
        return

    t.width(2 + int(5 * (side_length / initial_side_length)))
    t.pencolor(calculate_color(side_length, initial_side_length))

    for _ in range(4):
        t.forward(side_length)
        t.left(90)

    t.penup()
    t.backward(side_length / divisor / 2)
    t.right(90)
    t.forward(side_length / divisor / 2)
    t.left(90)
    t.pendown()

    draw_nested_squares(t, side_length / divisor, divisor, base_case, initial_side_length)
    t.penup()
    t.forward(side_length)
    t.pendown()
    draw_nested_squares(t, side_length / divisor, divisor, base_case, initial_side_length)
    t.penup()
    t.left(90)
    t.forward(side_length)
    t.right(90)
    t.pendown()
    draw_nested_squares(t, side_length / divisor, divisor, base_case, initial_side_length)
    t.penup()
    t.backward(side_length)
    t.pendown()
    draw_nested_squares(t, side_length / divisor, divisor, base_case, initial_side_length)

    t.penup()
    t.right(90)
    t.forward(side_length - side_length / divisor / 2)
    t.left(90)
    t.forward(side_length / divisor / 2)
    t.pendown()

def main():
    turtle.colormode(1.0)
    t = configure_turtle()
    initial_side_length = 200
    draw_nested_squares(t, side_length=initial_side_length, divisor=2, base_case=20, initial_side_length=initial_side_length)
    turtle.done()

if __name__ == "__main__":
    main()
