def fun(n):
    su=s=r=0
    while(1):
        s=0
        while(n!=0):
            r=n%10
            s=s+r
            n=n//10
        if s<10:
            su=s
            break
        else:
            n=s
            continue
    return su
            

n=int(input())
res=fun(n)
print(res)