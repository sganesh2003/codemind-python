def prime(n):
    c=0
    if n==1:
        return False
    for i in range(2,1+int(n**0.5)):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if prime(i)==True:
        c=c+1
print(c)