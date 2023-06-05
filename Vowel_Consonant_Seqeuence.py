s=input()
a=''
for i in s:
    if i not in "aeiou":
        if(len(a)==0):
            a+="C"
        elif(a[-1]!="C"):
            a+='C'
    else:
        if(len(a)==0):
            a+="V"
        elif(a[-1]!="V"):
            a+="V"
print(a)