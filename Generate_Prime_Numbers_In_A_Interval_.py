def prime(p):
    if(p>1):
        for i in range(2,int(p**(0.5))+1):
            if(p%i==0):
                return(0)
        else:
            return(1)
    else:
        return(0)


a=int(input())
b=int(input())
for i in range(a,b+1):
    if(prime(i)):
        print(i)