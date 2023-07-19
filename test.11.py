a=[]
b=["닭","토끼","돼지"]
l=[2,4,4]
s=0
for i in range(3):
    tmp=int(input(b[i]+"가축수:"))
    a.append(tmp)
    s += a[i]*l[i]
print(a)
print("다리합:",s)