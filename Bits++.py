x=0
for _ in range(int(input())):
    a=input()
    if("+" in a):
        x+=1
    else:
        x-=1
print(x)