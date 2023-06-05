n=int(input())
r=rev=d=rev=a=b=0
while(n!=0):
    r=n%10
    rev=rev*10+r
    n=n//10
while(rev!=0):
    a=rev%10
    rev=rev//10
    if d<1:
        if a==6:
            a=9
            d=1
    b=b*10+a
print(b)
        
    

    