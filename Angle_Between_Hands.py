t=input()
h=int(t[0:2])
m=int(t[3::])
hd=((h*60)+m)*(0.5)
md=m*6
d=abs(hd-md)
print(min(d,360-d))