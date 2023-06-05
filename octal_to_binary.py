a=input()
c=len(a)
s=0
for i in a:
    s=s+int(i)*(8**c)
    c=c-1
b=bin(s)
print(b[2:-3])