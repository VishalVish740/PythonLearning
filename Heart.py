from turtle import *

bgcolor("black")
color("red")
title("Heart Love")
begin_fill()
pensize(3)

# Move the turtle into position
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

penup()
goto(0, -50)
pendown()

# Set the text color and style
color("red")
write("I Love You", align="center", font=("Brush Script MT", 45, "normal"))
hideturtle()
done()