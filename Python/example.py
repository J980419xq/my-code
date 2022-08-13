n=1024
n=list(str(n))                     #['1', '0', '2', '4']
n=list(map(int,n))                 #[1, 0, 2, 4]
n=n[-1::-1]                        #[4, 2, 0, 1]
arr=[3,2,4,5,3]
arr2=sorted(set(arr))              #arr不变,arr2[2, 3, 4, 5]
arr.sort(reverse=True)             #arr变,reverse=True降序,默认升序
parent=list(range(4))              #[0,1,2,3]
map={"jxq":1,"yyh":2}
lst = list( map.items() )          #[('jxq', 1), ('yyh', 2)]