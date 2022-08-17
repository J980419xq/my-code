from audioop import add
from functools import reduce
from itertools import count, product, repeat
from random import choice
from re import M 
import string
from types import coroutine
from typing import Iterable


n=1024
n=list(str(n))                     #['1', '0', '2', '4']
n=list(map(int,n))                 #[1, 0, 2, 4]
n=n[-1::-1]                        #[4, 2, 0, 1]
arr=[3,2,4,5,3]
arr2=sorted(set(arr))              #arr不变,arr2[2, 3, 4, 5]
arr.sort(reverse=True)             #arr变,reverse=True降序,默认升序
str1=r'123\n'+'\\'
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
        print('私有方法','My lover is {}.'.format(self.__lover))
myclass=MyClass()
yyh=MyClass('yyh',22,'jxq')
print(range(19)[1])




