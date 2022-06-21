a,b=map(int,input().split())
for i in range(1,b+1):
    c=a*i
    if c%b==0:
        print("%d"%c)
        break