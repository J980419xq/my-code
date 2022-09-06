import collections

c=collections.Counter([1,2,3,1,2,3,1,1])   #字典的子类,计数可哈希对象,元素是key,计数为value Counter(【iterable|mapping】)<=>Counter({1:1,2:1,3:1})
print(c[0])                      #引用的键没有任何记录,就返回一个0,而不是弹出一个KeyError,也可以为负数 使用del移去一个元素 del c[2]    
'''c.elements() 返回一个迭代器,每个元素将重复出现计数值指定次,如果一个元素的计数值小于1,将会忽略它
c.most_common(【n】) 返回一个包含n个最常见的元素及出现次数(组合为元组)列表,按常见程度由高到低排序 n默认为None返回计数器中的所有元素 计数值相等的元素按首次出现的顺序排序
c.subtract(【iterable|mapping】) 减去iterable或mapping的元素 无返回值 原地修改
c.total() 计算总计数值
通常字典方法都可用于Counter对象 但update()作用改为添加元素 fromkeys()没有在Counter中实现'''
print(c)

dq=collections.deque('abcde',6)   #双向队列 deque(【iterable【,maxlen】】) maxlen默认为None增长到任意长度,否则限定为maxlen,满时新项加入则同样数量的项从另一端弹出
'''dq.append(x) 右端添加x dq.appendleft(x) 左端添加x dq.clear() 移除所有元素 dq.extend(iterable) 右侧添加iterable元素 dq.extendleft(iterable) 左侧添加iterable元素(逐个添加)
dq.copy() 创建一份浅拷贝 dq.count(x) 计算元素等于x的个数 dq.index(x【,lo【,hi】】) 返回x的索引(第一个匹配项),未找到则引发ValueError
dq.insert(i, x) 在位置i插入x,超出长度maxlen就引发一个IndexError dq.remove(value) 移除第一个value dq.reverse() 原地翻转deque
dq.pop() 移去并返回最右侧的元素,如果为空就引发一个IndexError dq.popleft() 移去并返回最左侧的元素
dq.rotate(n) 向右循环移动n步,n是负数就向左循环,默认为None等价于reverse() 向右循环移动一步等价于d.appendleft(d.pop()) 向左循环一步等价于d.append(d.popleft())
deque还支持迭代、封存、len(d)、reversed(d)、copy.copy(d)、copy.deepcopy(d)、in 以及下标引用(d[0])'''
print(dq)

d=collections.defaultdict(list)   #defaultdict(default_factory)使用default_factory提供的初始值的字典
'''d[k].append(v)
d = defaultdict(int)
def constant_factory(value):
    return lambda: value
d = defaultdict(constant_factory('<missing>'))'''