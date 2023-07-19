import turtle
turtle.shape("turtle")

color=("red","yellow","blue","green","purple")
dis=(1,3,5,2,8)
size=(2,1,6,3,5)
length=int(input("길이입력:"))

for i in range(5):
    turtle.pencolor(color[i])
    turtle.pensize(size[i])
    turtle.forward(length*dis[i])
    turtle.right(45)

turtle.done()