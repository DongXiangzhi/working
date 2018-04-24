import copy
a=[1,2,3,['a','b','c']]
b=a
c=copy.copy(a)
d=copy.deepcopy(a)

print(a,'\n',b,'\n',c,'\n',d)
a.append(5)
print(a,'\n',b,'\n',c,'\n',d)
a[3].append('fdasfasf')
print(a,'\n',b,'\n',c,'\n',d)