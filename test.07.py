a=[0,0,0,]
print(a)

d=[]
for i in range(3):
    d.append(0)
print(d)

# 리스트 표현inp
bb=[0 for i in range(100)]
print(bb)

# c=[0,0,0,0]
# s=0
# for i in range(4):
#     c[i].append(int(input("정수"+str(i+1)+":")))
#     s += c[i+3]
# print(c)
# print(s)


aa=[0,0,0,0]

aa[0]=int(input("정수1:"))
aa[1]=int(input("정수2:"))
aa[2]=int(input("정수3:"))
aa[3]=int(input("정수4:"))

hap=aa[0]+aa[1]+aa[2]+aa[3]
print("합:",hap)

aa=[]
hap=0
for i in range(4):
    tmp=int(input("정수"+str(i+1)+":"))
    aa.append(tmp)
    hap += aa[i]
print("합:",hap)
print(aa)