import turtle
import random

colors = ["#e9d996", "#dab832", "#c62750", "#93c3da", "#da94ad", "#bfe1e4", "#44a2be", "#46892e",
          "#f0eded", "#25225b"]

main_turtle = turtle.Turtle()
main_turtle.shape('circle')
screen = turtle.Screen()
main_turtle.speed('fastest')
main_turtle.penup()
main_turtle.goto(-250, -250)
main_turtle.speed('normal')

step = 10

while main_turtle.xcor() != 250.00 and main_turtle.ycor() != 300.00:
    main_turtle.color(random.choice(colors))
    main_turtle.pendown()
    main_turtle.dot(20)
    main_turtle.penup()
    main_turtle.forward(50)
    if main_turtle.xcor() == 250.0:
        main_turtle.setx(-250.0)
        y = main_turtle.ycor()
        main_turtle.sety(y + 50)
    if main_turtle.ycor() == 300:
        break


screen.exitonclick()