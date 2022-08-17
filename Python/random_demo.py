import random
random.seed (10*random.uniform(-100,100))   #设置随机数种子,生成的随机数将会是同一个
random.random()   #随机浮点数[0,1)
random.uniform(1,2)   #随机浮点数[a,b]
random.randint(2,5)   #随机整数[a,b]
random.randrange(-100,100,2)   #随机整数[a,b)且有步长c
random.choice('asd')   #从列表、元组或字符串中获取一个随机元素
random.shuffle([1,2,3])   #将列表中的元素打乱,无返回值 在原列表上修改
random.sample(sorted(map(int,'12345')),2,counts=[1,1,1,1,1])   #从序列中随机获取长度k的片断并随机排列,返回新列表 原序列不做修改 counts对应序列元素的个数
