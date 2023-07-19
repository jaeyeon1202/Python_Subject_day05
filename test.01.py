a=[]
b=list()
print(type(a),type(b))

c=[1,2,3,4,5]
print(c)
for i in range(5):
    print(c[i],end="")
print("")

d=["hello","python"]
print(d)
for i in range(2):
    print(d[i],end="")
print("")
print(d[1][0])

e=[1,2,"Hello",[10,20]]
print(e)
for i in range(len(e)):
    print(e[i],end="")
print("")
print(e[2][0],e[-1][0])

