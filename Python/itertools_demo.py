from itertools import *
import itertools

#无穷迭代器
it=itertools.count(1,2)   #count(start,[step]) start,start+step,start+2*step,...
it=itertools.cycle([1,2,3])   #重复迭代可迭代对象的元素 cycle(iterable) iter1,iter2...itern,iter1,iter2...
it=itertools.repeat(10,3)    #repeat(obj[,n]) 重复迭代任意指定对象n次或无限次 常用于在map或zip提供一个常量流
#由最短输入序列长度停止的迭代器
it=itertools.accumulate([1,2,3],lambda x,y:x+y*2) #accumulate(iterable[,func,initial=None]) 使用二元func对迭代序列进行累积 func默认为add,类似reduce(),不过返回的是每次op结果的迭代器
it=itertools.chain('ABC','DEF') #chain(*iterables) 首先返回第一个可迭代对象中所有元素,接着返回下一个可迭代对象中所有元素,直到耗尽所有可迭代对象中的元素
"chain可以接受多个迭代对象,chain.from_iterable可以接受一个元素为迭代对象的迭代对象"
it=itertools.chain.from_iterable(('ABC','DEF')) #chain.from_iterable(iterable)
it=itertools.compress('ABCDEF',[1,0,1,0,1,1]) #compress(data,selectors) (d[0] if s[0]),(d[1] if s[1])...输出data中经selectors真值测试为True的元素 都为可迭代对象
it=itertools.dropwhile(lambda x:x.islower(),"aAsdB") #丢掉首次predicate为False前的元素 dropwhile(predicate, iterable)
it=itertools.filterfalse(lambda x:x.islower(),"aAsdB") #只返回iterable中predicate为False的元素 filterfalse(predicate, iterable)
it=itertools.groupby([1,4,7,10,2,5,3,6,1],key=lambda x:x%3) #返回键和组,组内也为迭代器 groupby(iterable, key=None) for ket group in it
it=itertools.islice('ABCDEFG', 2, None) #islice(iterable[,start],stop[, step]) 与普通的切片不同,islice不支持将start,stop,step设为负值
it=itertools.pairwise('ABCDEFG') #输出iterable中的连续重叠对 pairwise(iterable) -->AB BC CD DE EF FG
it=itertools.starmap(pow,[[2,5,3],[3,2],[10,3]]) #starmap(function,iterable) 使用从序列中获取的参数来计算该函数并返回函数结果 -->32 9 1000 比map可接受参数能力强
it=itertools.takewhile(lambda x: x<5, [1,4,6,4,1]) #takewhile(predicate, iterable) 与dropwhile相反 输出直到pred真值测试失败前的元素 -->1 4
#由最长输入序列长度停止的迭代器
it=itertools.zip_longest('ABCD','xy',fillvalue='-') #zip_longest(*iterables,fillvalue=None) 从每个可迭代对象中收集元素,根据fillvalue填充缺失值
#排列组合迭代器
"product(*iterables[,repeat=1]) 笛卡儿积 类似于生成器表达式中的嵌套for循环,product(A,B)和((x,y) for x in A for y in B)返回结果一样"
it=itertools.product(range(2),repeat=3)   #(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)
"permutations(iterable,r=None)长度r元组,所有可能的排列,无重复元素"
it=itertools.permutations('ABCD',2) # AB AC AD BA BC BD CA CB CD DA DB DC 不同位置的元素也被认为是不同的
"combinations(iterable,r)长度r元组,有序,无重复元素"
it=itertools.combinations('ABCD', 2)# AB AC AD BC BD CD 不同位置的元素也被认为是不同的
"combinations_with_replacement(iterable, r)长度r元组,有序,元素可重复"
it=itertools.combinations_with_replacement('ABCD', 2) #不同位置的元素是不同的
for i in it:
    print(i)

