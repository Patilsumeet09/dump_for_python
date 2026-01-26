l=[1,4,6,9,22]
f=0
s=1
mx=0
for i in range(0,len(l)-1):
    if l[f]>l[s]:
        mx=l[f]
    else:
        mx=l[s]
        f=f+1
        s=s+1
print(mx)