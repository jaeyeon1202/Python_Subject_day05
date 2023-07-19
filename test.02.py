a="good"
b=["g","o","o","d"]
c=("g","o","o","d")

for i in range(len(a)):
    print(a[i],end="")
print("")


for i in range(len(b)):
    print(b[i],end="")

print("")
b[0]="k"
print(b)

for i in range(len(c)):
    print(c[i],end="")
print("")
