import math
n=int(input())
ar=[]
for i in range(100):
    ar.append(pow(2,i))
f=l=df=dl=0
for i in range(100):
    if ar[i]>n:
        f=ar[i-1]
        l=ar[i]
        df=n-f
        dl=l-n
        print(min(df,dl))
        break
    