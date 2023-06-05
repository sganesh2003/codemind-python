n=int(input())
x=n
r=0
rev=0
if n<0:
    n=n*-1
if(n>0):
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
if(x>0):
    print(rev)
else:
    print(rev*-1)
    
    