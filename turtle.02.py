import turtle
turtle.shape("turtle")

dis=int(input("라인길이:"))

color=["red","blue","purple"]
size=[2,7,9]

for i in range(3):
    turtle.pencolor(color[i])
    turtle.pensize(size[i])
    turtle.forward(dis)
    turtle.right(90)
turtle.done()
    