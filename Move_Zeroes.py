n=list(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if i!=0:
        l.append(i)
for i in a:
    if i==0:
        l.append(i)
print(*l)