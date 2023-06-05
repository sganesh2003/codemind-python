def fun(n):
    pal=n[::-1]
    return pal
t=int(input())
for i in range(t):
    n=input()
    x=fun(n)
    if(int(n)==int(x)):
        print("True")
    else:
        print("False")
        