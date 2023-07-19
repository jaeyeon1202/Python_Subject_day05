import turtle
turtle.shape("turtle")

color=["red","blue","purple"]
for i in range(3):
    turtle.pencolor(color[i])
    turtle.forward(100)
    turtle.left(120)
turtle.done()