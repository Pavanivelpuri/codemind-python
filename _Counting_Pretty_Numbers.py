n=int(input())
for i in range(n):
    X,Y=map(int,input().split())
    c=0
    for i in range(X,Y+1):
        r=i%10
        if(r==2 or r==3 or r==9):
            c=c+1
    print(c)