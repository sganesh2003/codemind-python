def fact(p):
    if(p==1 or p==0):
        return(1)
    else:
        return(fact(p-1)*p)
n=int(input())
for i in range(n):
    a=int(input())
    print(fact(a))