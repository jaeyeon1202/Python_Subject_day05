import turtle
turtle.shape("turtle")

a=[100,40,30,70,10,90]
c=["red","blue","yellow","orange","pink","purple"]
dis=int(input("길이:"))
s=0
for i in range(len(c)):
    turtle.pencolor(c[i])
    turtle.forward(dis)
    turtle.up()
    s=s+a[i]
    turtle.goto(0,s)
    turtle.down()
turtle.done()

#부분합 형태 * 
# s=0
# s += a[i]
# print(s)