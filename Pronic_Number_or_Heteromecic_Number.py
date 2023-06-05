n=int(input())
c=0
for i in range(n):
    if(i*(i+1)==n):
            c=1
            break
if(c==1):
    print("YES")
else:
    print("NO")