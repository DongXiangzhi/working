mstr='Hello world,i am using Python to programeeeeeeee'
mList=list(mstr)
mdict={}
for e in mList:
    if mdict.get(e,-1)==-1:
        mdict[e]=1
    else:
        mdict[e]+=1
for key,value in mdict.items():
    print(key,value)


print(mdict.items())
print(len(mdict.items()))
