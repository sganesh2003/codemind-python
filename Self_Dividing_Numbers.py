def sel(n):
    x=n
    f=0
    d=r=p=0
    while(n!=0):
        r=n%10
        d=d+1
        if(r!=0 and x%r==0):
            p=p+1
        n=n//10
    if d==p:
        f=1
    return f
n=int(input())
m=int(input())
for i in range(n,m+1):
    if sel(i)==1:
        print(i,end=" ")
    
    
    