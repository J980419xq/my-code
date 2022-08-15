### 内置函数
```python
'''[可迭代对象iterable(字符串、列表、元组、集合、字典...)[迭代器iterator[生成器generator]]]
可迭代对象都构建了__iter__()方法,迭代器另外实现__next__()方法,生成器使用yield或者生成器表达式(将列表表达式的`[]`换成`()`) g = (x * x for x in range(10))
可变对象 list、dict、set 对象的内容是可以变化的,且发生变化时对象的引用是不会变化
不变对象 tuple、string、int、float、bool、None 调用对象自身的任意方法,都不会改变对象的内容,变的只是创建了新对象,改变了对象的引用'''
isinstance(isinstance(example,(set,tuple)))   '''类型匹配 返回值bool'''   type(example)   '''既可以返回一个对象的类型'''   dir(example)   '''获得一个对象的所有属性和方法,返回一个包含字符串的list'''
Hello = type('Hello', (object,), dict(hello=fn))   #创建新类型Hello,1.class的名称2.继承的父类,元组传入3.class的方法名称与函数绑定
num=ord(c)-ord('a') chr(97)   #互为逆操作
max(1,2,3)    len(str1)       min(lst)   gcd(1,2【,3,4...】)   sum(iterable【,initial_value】)
math.ceil(x)   '''求大于等于x的最小整数'''   divmod(a,b)   '''返回一个包含商和余数的元组(a // b, a % b)'''
str1=r'123\n'+'\\'                   #r|R标识原始字符串,此时'\'不做转义,但'\'不可做结尾,单独另写结尾的'\'
10_000_000_000==10000000000   '''`==`比较值 `is`比较id'''   '''`**`幂运算符,`//`整除运算符'''   a,b,c=1,2,3   a,b=b,a
''' `and` `or` `not` `in` `not in` `is` for _ in iterable: if: elif: else: while: sign = 1 if c == '+' else -1'''   
int('011',2)   '''将二进制字符串转成int'''    hex(16)   '''把一个整数转换成十六进制字符串'''   
enumerate()   '''用于将一个可遍历的数据对象变成索引-元素对'''   for i, value in enumerate(['A', 'B', 'C']):
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
sorted(iterable【,key=op,reverse=False】)   #op:一元函数用于序列的每一个元素上 对op返回的结果进行排序,返回一个新序列 reverse:默认为False(升序)
    sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})   #list.sort()方法只为list定义并且在原list上排序,而sorted()可以接收任何的iterable
product(*iterables【,repeat】)   #类似于生成器表达式中的嵌套循环,product(A,B)和((x,y) for x in A for y in B)返回结果一样
    product(range(2),repeat=3)   #(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)
bisect.bisect_left(a,x,【lo=0,hi=len(a),key】)   #定位x在有序序列a中的插入点,lo和hi用于指定查找区间,key作用于每个元素,如果x已经存在于a中,那么插入点在已存在元素的左边,返回值是序列下标,bisect_right()<=>bisect()返回的插入点是a中已存在元素x的右侧
bisect.insort_left(a,x【,lo=0,hi=len(a),key】)   #将x插入有序序列a内,相当于a.insert(bisect.bisect_left(a, x, lo, hi), x)
choice(iterable)   #返回含有len()的序列的随机项 random.choice(range(100))
zip(【iterable,...】)   #将可迭代的对象中对应的元素打包成一个个元组,然后返回由这些元组组成的对象,返回长度与最短的序列相同,利用 * 号操作符,可以将元组解压为列表
    zip([1,2,3],[4,5,6,7])   #(1, 4), (2, 5), (3, 6)   *zip([1,2,3],[4,5,6,7]) `*`解压zip为多个序列<=>a,b,c=zip([1,2,3],[4,5,6,7])
input(【prompt】)   #prompt:提示信息 接受一个标准输入数据,返回为 string 类型 input("input:")
```

## list [] 元素之间有顺序
```python
lst=[1,"a",[2,3]]   list(iterable)   cmp(lst1,lst2)   '''返回-1,0,1'''   len(lst)   max(lst)   min(lst)   
['Hi!'] * 4   '''['Hi!', 'Hi!', 'Hi!', 'Hi!']'''   lst.reverse()   '''lst反向'''
lst.index(x【,lo【,hi】】)   #返回第一次匹配x的索引位置,如果没有找到对象则抛出异常
lst[start【:stop【:step】】]   #step为负数时从后往前切 stop为待切序列后一项同
lst.count(x【,lo【,hi】】)   '''返回x出现次数'''   lst.append(x)   '''末尾添加x'''   lst.extend(iterable)   '''在末尾添加多个元素 lst1+lst2<=>lst1.extend(lst2)'''   lst.insert(inex,x)   '''在指定索引位置插入x'''
lst.remove(x)   '''移除第一个x'''   lst.pop(【index】)   '''移除指定索引元素,不指明则删除最后一个'''   lst.clear()   '''清空列表'''  del lst[1]   lst.del()   '''删除列表'''
lst.sort(【key,reverse】)   #reverse和key同sorted()
lst=[i*i for i in range(5) if i%2==1]   lst=[m + n for m in 'ABC' for n in 'XYZ']   #列表生成式
lst=[[0 for x in range(10)] for y in range(10)]   #二维列表 lst=[[False]*n for _ in range(n)] 
```

## string ' '|''' '''|" "
```python
'我叫%s,今年%d岁' % (name,age)   #<=>'我叫{0},今年{1}岁'.format(name,age)<=>f'我叫{name}，今年{age}岁' '%%'输出一个单一的'%'
str1.index() str1.count() max(str1) min(str1)  #同list
str1.split(str,num)   #使用str(默认空字符)对str1进行切片 num:分隔num次 返回分割后的字符串列表 rsplit() 从右边开始分割
str1.find(str2【,lo,hi】)   #返回str1指定区间中第一个str2的开始索引位置,不存在则返回-1 str1.index() str1.rfind() str1.rindex()
str1.upper()/lower()/swapcase()/title()/capitalize()  #大写/小写/大小写转换/每个单词第一个大写其余小写/第一个大写其余小写
str1.isalpha()/isdecimal()/isnumeric()/isalnum()/isdigit()/isspace()/issupper()/islower()/istitle()/isidentifier()   #字母/十进制数字/数字/字母和数字/数字/空白字符/大写/小写/标题化/合法标识符
str1.center/ljust/rjust(width【,fillchar】)   #原字符串居中,并使用fillchar(默认为空格)填充至width的新字符串 左对齐 右对齐 zfill(width) 用'0'填充右对齐
str1.decode(encoding,errors】)   #以encoding指定的编码格式解码字符串 errors:设置错误的处理方案 str1.encode(encoding【，errors】)
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
