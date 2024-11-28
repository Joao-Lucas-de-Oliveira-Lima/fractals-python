import turtle

def set_color(side_length, initial_side_length):
    intensity = side_length / initial_side_length
    adjusted_intensity = max(0.4, intensity)
    return (adjusted_intensity, 0.1, 0.1)

def draw_squares(side_length, divisor, base_case, initial_side_length):
    if side_length >= base_case:
        turtle.width(2 + int(5 * (side_length / initial_side_length)))
        turtle.pencolor(set_color(side_length, initial_side_length))
        
        for _ in range(4):
            turtle.forward(side_length)
            turtle.left(90)
        
        turtle.penup()
        turtle.forward(-side_length / divisor / 2)
        turtle.right(90)
        turtle.forward(side_length / divisor / 2)
        turtle.left(90)
        turtle.pendown()

        draw_squares(side_length / divisor, divisor, base_case, initial_side_length)
        turtle.penup()
        turtle.forward(side_length)
        turtle.pendown()
        draw_squares(side_length / divisor, divisor, base_case, initial_side_length)
        turtle.penup()
        turtle.left(90)
        turtle.forward(side_length)
        turtle.right(90)
        turtle.pendown()
        draw_squares(side_length / divisor, divisor, base_case, initial_side_length)
        turtle.penup()
        turtle.forward(-side_length)
        turtle.pendown()
        draw_squares(side_length / divisor, divisor, base_case, initial_side_length)

        turtle.penup()
        turtle.right(90)
        turtle.forward(side_length - side_length / divisor / 2)
        turtle.left(90)
        turtle.forward(side_length / divisor / 2)
        turtle.pendown()

screen = turtle.Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
turtle.speed(0) 
turtle.hideturtle()
turtle.penup()
turtle.goto(0, -90)
turtle.pendown()
turtle.width(10)

initial_side_length = 200
turtle.left(90)
draw_squares(initial_side_length, 2, 20, initial_side_length)
turtle.done()
