### 内置函数
```python
'''[可迭代对象iterable(字符串、列表、元组、集合、字典...)[迭代器iterator[生成器generator]]]
可迭代对象都构建了__iter__()方法,迭代器另外实现__next__()方法,生成器使用yield或者生成器表达式(将列表表达式的`[]`换成`()`) g = (x * x for x in range(10))
可变对象 list、dict(key不可变)、set 对象的内容是可以变化的,且发生变化时对象的引用是不会变化
不变对象 tuple、string、int、float、bool、None 调用对象自身的任意方法,都不会改变对象的内容,变的只是创建了新对象,改变了对象的引用'''
isinstance(isinstance(example,(set,tuple)))   '''类型匹配 返回值bool'''   type(example)   '''既可以返回一个对象的类型'''   dir(example)   '''获得一个对象的所有属性和方法,返回一个包含字符串的list'''
Hello = type('Hello', (object,), dict(hello=fn))   #创建新类型Hello,1.class的名称2.继承的父类,元组传入3.class的方法名称与函数绑定
num=ord(c)-ord('a') chr(97)   #互为逆操作
max(1,2,3)    len(str1)       min(lst)   gcd(1,2【,3,4...】)   sum(iterable【,initial_value】) reversed(iterable) '''翻转序列返回一个迭代器'''
math.ceil(x)   '''求大于等于x的最小整数'''   divmod(a,b)   '''返回一个包含商和余数的元组(a // b, a % b)'''
str1=r'123\n'+'\\'                   #r|R标识原始字符串,此时'\'不做转义,但'\'不可做结尾,单独另写结尾的'\'
10_000_000_000==10000000000   '''`==`比较值 `is`比较id'''   '''`**`幂运算符,`//`整除运算符'''   a,b,c=1,2,3   a,b=b,a   a=(1)<=>a=1
''' `and` `or` `not` `in` `not in` `is` for _ in iterable: if: elif: else: while: sign = 1 if c == '+' else -1'''   
int('011',2)   '''将二进制字符串转成int'''    hex(16)   '''把一个整数转换成十六进制字符串'''   
enumerate()   '''用于将一个可遍历的数据对象变成索引-元素对'''   for i, value in enumerate(['A', 'B', 'C']):   del obj   #删除一个完整对象
range(start,stop,step)   #整数序列[start,stop)步长step    
lambda x,y:x+y   #lambda只允许包含一个表达式,可以接收任意多个参数(包括可选参数),该表达式的运算结果就是函数的返回值  
g=[lambda a:a*2,lambda b:b*3]   #定义了两个2个lambda函数元素的列表,可通过g[0](1)、g[1](5)调用
map(op,iterable1【,iterable2,...】)   #op:函数名,多为lambda表达式 对参数序列中的每一个元素调用op,取短序列截断,返回迭代器
    map(lambda x, y: x+y, [4,5,6], [1,2,3])
reduce(op,iterable【,initial_value】)   #把一个二元函数作用在一个序列上,把结果继续和序列的下一个元素做累积计算,返回op最后的返回值
    reduce(or_, (num for j, num in enumerate(nums) if (i >> j) & 1), 0)
filter(op,iterable)   #使用op过滤序列中不符合条件的元素,返回一个iterator
    newlst=list(filter(lambda x:x%2==1,[1,2,3,4]))
all(iterable)   #判断序列中的所有元素是否都为true(不为0、''、False或者为空),如果是返回True,否则返回False
any(iterable)   #判断序列中的所有元素是否都为false,如果是返回false,否则有一个为True则返回True
eval(expression【,globals【,locals】】)   #globals:全局命名空间,必须是字典对象 locals:局部命名空间,任何映射对象 执行一个字符串表达式
    eval('pow(2,2)')   #返回表达式计算结果,此处为4(int)
sorted(iterable【,key=op,reverse=False】)   #op:一元函数用于序列的每一个元素上 对op返回的结果进行排序,返回一个新列表 reverse:默认为False(升序)
    sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})   #list.sort()方法只为list定义并且在原list上排序,而sorted()可以接收任何的iterable
zip(【iterable,...】)   #将可迭代的对象中对应的元素打包成一个个元组,然后返回由这些元组组成的对象,返回长度与最短的序列相同,利用 * 号操作符,可以将元组解压为列表
    zip([1,2,3],[4,5,6,7])   #(1, 4), (2, 5), (3, 6)   *zip([1,2,3],[4,5,6,7]) `*`解压zip为多个序列<=>a,b,c=zip([1,2,3],[4,5,6,7])
input(【prompt】)   #prompt:提示信息 接受一个标准输入数据,返回为 string 类型 input("input:")
bisect.bisect_left(a,x,【lo=0,hi=len(a),key】)   #定位x在有序序列a中的插入点,lo和hi用于指定查找区间,key作用于每个元素,如果x已经存在于a中,那么插入点在已存在元素的左边,返回值是序列下标,bisect_right()<=>bisect()返回的插入点是a中已存在元素x的右侧
bisect.insort_left(a,x【,lo=0,hi=len(a),key】)   #将x插入有序序列a内,相当于a.insert(bisect.bisect_left(a, x, lo, hi), x)
heapq.heapify(lst)   #将列表转换成堆,原地转换 空堆就是一个空列表[] 实现的是小根堆 heapq._heapify_max(lst)实现的是大根堆
heapq.heappush(heap, item)   #将item的值加入heap中 无返回值 保持堆的不变性
heapq.heappop(heap)   #弹出并返回heap的最小的元素,保持堆的不变性,如果堆为空,抛出IndexError 
heapq.heappushpop(heap, item)   #将item放入堆中,然后弹出并返回heap的最小元素
heapq.heapreplace(heap, item)   #弹出并返回heap中最小的一项,然后加入新的item,堆的大小不变,如果堆为空则引发IndexError
heapq.merge(*iterables,key=None,reverse=False) #将多个已排序的输入合并为一个排好序的输出,返回一个生成器 key和reverse类似sorted用法
heapq.nlargest(n, iterable, key=None)   #返回iterable序列前n个最大元素组成的列表 <->sorted(iterable, key=key, reverse=True)[:n]
heapq.nsmallest(n,iterable, key=None)   #返回iterable序列前n个最小元素组成的列表
```

## list [] 
```python
lst=[1,"a",[2,3]]   list(iterable)'dict只保留key'   cmp(lst1,lst2)   '''返回-1,0,1'''   len(lst)   max(lst)   min(lst)   
['Hi!'] * 4   '''['Hi!', 'Hi!', 'Hi!', 'Hi!']'''   lst.reverse()   '''lst反向'''
lst.index(x【,lo【,hi】】)   #返回第一次匹配x的索引位置,如果没有找到对象则抛出异常
lst[start【:stop【:step】】]   #step为负数时从后往前切 stop为待切序列后一项同
lst.count(x【,lo【,hi】】)   '''返回x出现次数'''   lst.append(x)   '''末尾添加x'''   lst.extend(iterable)   '''在末尾添加多个元素 lst1+lst2<=>lst1.extend(lst2)'''   lst.insert(inex,x)   '''在指定索引位置插入x'''
lst.remove(x)   '''移除第一个x'''   lst.pop(【index】)   '''移除指定索引元素,不指明则删除最后一个'''   lst.clear()   '''清空列表'''  del lst[1]   '''删除列表索引值'''
lst.sort(【key,reverse】)   #reverse和key同sorted()
lst=[i*i for i in range(5) if i%2==1]   lst=[m + n for m in 'ABC' for n in 'XYZ']   #列表生成式
lst=[[0 for x in range(10)] for y in range(10)]   #二维列表 lst=[[False]*n for _ in range(n)] 
```

## string ' '|''' '''|" "
```python
'我叫%s,今年%d岁' % (name,age)   #<=>'我叫{0},今年{1}岁'.format(name,age)<=>f'我叫{name},今年{age}岁' '%%'输出一个单一的'%'
str1.index() str1.count() max(str1) min(str1) str(obj)   #同list且支持切片 str()会将一个对象完整表示为字符串 str([1,2,3])<=>"[1,2,3]"
str1.split(str,num)   #使用str(默认空字符)对str1进行切片 num:分隔num次 返回分割后的字符串列表 rsplit() 从右边开始分割
str1.find(str2【,lo,hi】)   #返回str1指定区间中第一个str2的开始索引位置,不存在则返回-1 str1.index() str1.rfind() str1.rindex()
str1.upper()/lower()/swapcase()/title()/capitalize()  #大写/小写/大小写转换/每个单词第一个大写其余小写/第一个大写其余小写
str1.isalpha()/isdecimal()/isnumeric()/isalnum()/isdigit()/isspace()/issupper()/islower()/istitle()/isidentifier()   #字母/十进制数字/数字/字母和数字/数字/空白字符/大写/小写/标题化/合法标识符
str1.center/ljust/rjust(width【,fillchar】)   #原字符串居中,并使用fillchar(默认为空格)填充至width的新字符串 左对齐 右对齐 zfill(width) 用'0'填充右对齐
str1.decode(encoding,errors】)   #以encoding指定的编码格式解码字符串 errors:设置错误的处理方案 str1.encode(encoding【,errors】)
str1.endswith(suffix【,lo【,hi】】)   #判断str1指定区间内是否以suffix结尾,返回bool类型 startwith() 开头
str1.join(iterable)   #将元素为字符串的序列以指定的字符str1连接生成一个新的字符串 ":".join(map(str,[1,2,3]))
str1.strip/lsrip/rstrip(【chars】)   #移除字符串头尾的chars(默认为空白字符) 开头 结尾 
str1.partition(str2)   #使用str2将str1进行分割,返回一个(左边子串,str2,右边子串)的3元元组,如果str2不存在,返回(str1,",") rpartition从右边开始搜索
str1.replace(old, new【,max】)   #将str1的old字符串替换成new字符串,替换不超过max次(默认全部替换),返回新字符串
#zlib压缩解压字符串
import zlib
t = zlib.compress(b'hello world!hello world!hello world!hello world!')
print(t)  #b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'
print(zlib.decompress(t))  #b'hello world!hello world!hello world!hello world!'
```

## tuple () (1,) 
```python
tuple(iterable)   #将序列转为元组 元组元素不可修改,但可以拼接形成一个新元组 元组中list元素值可变 任意以逗号隔开的无符号对象视为元组 函数返回多值就是返回一个元组
a,*b,c=[1,2,3,4]   #元组解包 a=1,b=[2,3],c=4 集合可能顺序不同,字典只解key,加上.items()解包成元组
len(tup) ('Hi!',)*4<=>('Hi!', 'Hi!', 'Hi!', 'Hi!') cmp(tup1,tup2) max(tup) min(tup) (1,2,3)+(4,5,6)   #同list且支持切片
```

## dict {} {key1 : value1, key2 : value2 } 
```python
dict(x=5, y=0,key=value) {'x':5,'y':0,key:value}   #key通常唯一,重复的key-value对取最后一次的value 关键字参数创建字典 使用映射来创建字典 会记住元素插入顺序
dict([('x',5),['y',0],(key,value)]) dict(zip(['x','y',key],[1,2,value]))  #使用二元可迭代对象(元素为长度为2的序列)创建字典 最多两种方式同时使用 且第二种只能是关键字
dic.fromkeys(iterable【,value】)   #返回一个新字典,以序列中的每个元素做键映射同一value(默认为None) value为浅拷贝,都是同一引用
dic.get(key【,value】)   #返回指定键的值,不存在时返回value(默认None) key不存在的时候,setdefault()会返回默认值并更新字典添加键值,而get()只返回默认值,并不改变原字典
dic.setdefault(key【,default】)   #key在字典中,返回对应的值,如果不在字典中,则插入key-default对,并返回default,default默认值为None
dic.update(dict2)   #dict2的key/value对更新到dic里
dic.keys() dic.values() dic.items()   #获取可遍历的键/键值/键值对的视图对象,不可修改,不支持索引
dic.clear() len(dic) del dist[key]   #同list 字典的长度为key的个数 添加键值对为dic[key]=value
dic.pop(key【,default】)   #删除key所对应的值,返回被删除的值,如果key不存在,返回default,如果default也没有指定,触发 KeyError 异常
dic.popitem()   #删除最末尾的键值对
dic={key:len(key) for key in ['Google','Runoob','Taobao']} dic={key:value for key,value in zip(lst1,lst2)}   #字典生成式
dic={key:value for key,value in sorted(dic.items(),key=lambda x:x[0],reverse=True)}   #字典排序
```

## set {} {value1,value2}
```python
set(iterable) len(s) min(s) len(s) s.clear()   #创建一个空集合必须用set(),因为{}用来创建一个空字典 无序不重复且元素为不可变对象
s={i*i for i in range(10)}   #集合生成式
s.add(obj)   #obj为不可变对象
s.update(iterable,iterable2...)   #添加序列中s没有的元素,这些元素也必须为不可变对象
s1.difference(s2)   #差集s1-s2(返回一个新集合,元素在s1中,但不在s2) s1.symmetric_difference(s2) 对称差集s1^s2(两个集合中不重复的元素集合)
s1.difference_update(s2)   #移除s1中s2也存在的元素,无返回值原地修改 s.intersection_update(s1,s2...) s.symmetric_difference_update(s1)
s1.intersection(s2,s3...)   #交集s1&s2,返回一个新集合,可以是其他iterable,字典则为key s1.union(s2,s3...)并集s1|s2
s.isdisjoint(s1)   #判断两个集合是否包含相同的元素,没有返回True,否则返回False s.issubset(s1) s是s1的子集 s.issuperset(s1) s是s1的超集
s.discard(value)   #移除value不存在也不会报错 s.remove(value) value不存在会报错
s.pop()   #随机移除一个元素
```

## 函数
python中不可变类型参数类似值传递,可变类型类似引用传递<br>
函数定义中参数前的`*`表示的是将调用时的多个参数放入元组中,`**`则表示将调用时的关键字参数放入一个字典中<br>
函数调用中,`*`表示将可迭代对象中的所有元素解包(unpack)变成位置参数,`**`表示将字典扩展为关键字参数<br>
必需参数、可变参数、关键字参数,默认参数必须指向不变对象<br>
偏函数`functools.partial()`把一个函数的某些参数给固定住(也就是设置默认值),返回一个新的函数<br>
`/`前只能用位置参数 `*`后只能用关键字参数
```python
def now(time):
    def sayName(func):                                  #装饰器输出
        def inner(name):                                #now: 2016/10/30
            print('now: %s'% time)                      #I'm Yu
            print("I'm Yu")                             #Hello,siri
            return func(name)
        return inner
    return sayName
@now('2016/10/30')
def sayHi(name):
    print('Hello,' + name)
sayHi('siri')
```
```python
def sayName(func):                                     #输出
    print('name')                                      #age
    def inner():                                       #name
        print("I'm Yu")                                #I'm Yu
        return func()                                  #i'm 30
    return inner                                       #Hello, World

def sayAge(func):
    print('age')
    def inner():
        print("i'm 30")
        return  func()
    return inner

@sayName
@sayAge
def sayHi():
    print('Hello, World')
sayHi()
```

## 类
```python
class MyClass:
    count=0                         #类属性 每个实例都可访问,但实例修改只会创建一个实例属性,统一修改需要使用MyClass.count+=1
    __slots__ = ('name', 'age' ,'__lover') # 用tuple定义允许绑定的属性名称,只对当前类起作用,继承的子类不受限制 
    def __init__(self,name='jxq',age=23,lover='yyh'):   #构造方法,类实例化时自动调用
        self.name=name
        self.age=age
        self.__lover=lover   #私有变量,无法从类外部访问 私有方法也以`__`开头 `_`开头不是私有变量,但不要随意访问
        MyClass.count+=1
    def fun(self):
        self.__privateFun()
    @staticmethod                                        #静态方法,类和对象都能使用
    def staticFun():
        print('静态方法',MyClass.count)
    @classmethod                                         #类方法,类和对象都能使用
    def classFun(cls):
        print('类方法',cls.count)
    def __privateFun(self):                              #私有方法类外部无法使用
        print('私有方法','My lover is {}'.format(self.__lover))
```

## 错误和异常
```python
try:                                                #执行try子句,无异常发生忽略except子句,发生异常则try子句余下的部分将被忽略
    fenzi,fenmu=map(int,input().split(" "))
    ans=fenzi/fenmu
except Exception as e:                              #执行异常处理
    print('error as for {}'.format(e))
else:                                               #try没发生异常时执行
    print(ans)
finally:                                            #不管有没有异常都要执行
    print("now is finished")
raise Exception('x不能大于5,x的值为:{}'.format(x))   #抛出异常raise [Exception [, args [, traceback]]]
assert 1==2,'1不等于2'   #断言,表达式为False时抛出异常 assert expression [,arguments]=>raise AssertionError(arguments)
''' with 语句用于异常处理,封装了 try…except…finally 编码范式,提高了易用性 
with open('./test_runoob.txt', 'w') as file:
    ...
'''
```