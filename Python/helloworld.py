import random
n=256
'''n=str(n)
n=[int(i) for i in n]
'''
print(random.random())
n=list(map(int,list(str(n))))
print(n[-1::-1])
arr=[3,2,4,5,3]
for i,v in enumerate(sorted(set(arr)),1):
    print(i,v)
print(arr)
parent=list(range(4))    #[0,1,2,3]
map={"jxq":1,"yyh":2}
lst = list( map.items() )
print(lst)
