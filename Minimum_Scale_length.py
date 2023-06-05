n=int(input())
l=list(map(int,input().split()))
a=min(l)
c=[]
for i in range(1,int(a**(0.5))+1):
    if(a%i==0):
        c.append(i)
        if(i!=(a//i)):
            c.append(a//i)
c.sort()
c=c[::-1]
for j in c:
    for k in l:
        if(k%j!=0):
            break
    else:
        print(j)
        break