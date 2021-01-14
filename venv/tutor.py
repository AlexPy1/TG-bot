a=int(input())
b=[]
y=""
c=0
e=-1
for i in range(a):
    b+=[str(i)]*i
    if len(b)>=a:
        break
if len(b)>=a:
    for i in range(len(b)):
        if i>=a:
            b.remove(b[e])
for i in b:
    y+=str(i)+" "
if a==1:
    print(1)
print(y)