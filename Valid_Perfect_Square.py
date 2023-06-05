import math 
n=int(input())
for l in range(n):
    m=int(input())
    c=0
    for i in range(1,m+1):
        if i*i==m:
            c=1
    if c==1:
        print("True")
    else:
        print("False")
        