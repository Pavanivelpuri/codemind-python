n=int(input())
a=list(map(int,input().split()))
f=0
s=len(a)
for i in range(0,s):
    f=f+a[i]
print(f)