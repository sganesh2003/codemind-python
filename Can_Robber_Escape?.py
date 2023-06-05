n=int(input())
ls=list(map(int,input().split()))
r=0
for i in range(len(ls)):
    if(ls[i]%2!=0):
        r=r+1
if(r<=2):
    print("YES")
else:
    print("NO")