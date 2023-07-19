a=[]
b=["국어","영어","수학"]
s=0
for i in range(3):
    num=int(input(b[i]+"점수:"))
    a.append(num)
    s += a[i]
avg=s/3
print("총점:",s)
print("평균: %.2f" % avg)

    