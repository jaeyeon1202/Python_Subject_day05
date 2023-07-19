import turtle
import random
turtle.shape("turtle")

length=int(input("길이:"))
color=["red","yellow","blue","green","purple"]
dis=[1,3,5,2,8]

for i in range(5):
    # turtle.pencolor(random.choice(color))
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.pencolor((r,g,b))
    turtle.pensize(random.randint(1,10)) #초이스 or 랜덤함수
    turtle.forward(length/dis[i])
    turtle.right(45)
turtle.done()

