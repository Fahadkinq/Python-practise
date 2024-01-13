a=[1,2]
b=a
c=a[:]
d=list(a)
a[0:2]=[4,3]    
print(a+[6,7])
print(a+b)
print(a,b,c,d)

print(a)
print(len(a))
a.reverse()
print(a)