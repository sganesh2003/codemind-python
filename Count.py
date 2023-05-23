
n=int(input())
lt=list(map(int,input().split()))
x=0
y=0
for i in lt:
    if i%2==0:
        x+=1
    else:
        y+=1
print(x,y,end=' ')
