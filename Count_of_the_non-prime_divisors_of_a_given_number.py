def prime(p):
    if(p>1):
        for i in range(2,int(p**(0.5))+1):
            if(p%i==0):
                return(0)
        else:
            return(1)
    else:
        return(0)

n=int(input())
c=0
for i in range(1,int(n**(0.5))+1):
    if(n%i==0):
        if(prime(i)==False):
            c+=1
        if(i!=(n//i)):
            if(prime(n//i)==False):
                c+=1
print(c)