def rev(n):
    r=0
    rev=0
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
def prime(n):
    c=0
    f=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        f=1
    return f
n=int(input())
if prime(n)==1:
    if prime(rev(n))==1:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")