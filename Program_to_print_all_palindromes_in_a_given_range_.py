def palin(p):
    a=str(p)
    if(str(p)==a[::-1]):
        return(1)
    else:
        return(0)

n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    if(palin(i)==1):
        print(i,end=" ")