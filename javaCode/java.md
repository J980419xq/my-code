## idea快捷键
shift+shift 打开搜索框，全局搜索  
alt+enter 快速修复  
shift+F10 运行代码， shift+F9 debug代码，ctrl+F8 设置断点    
psvm 快捷键生成 main 函数，sout 输出语句 ctrl+p 提示构造方法属性 ctrl+alt+b 跳转到方法实现处
ctrl+/ 单行注释， ctrl+shift+/ 多行注释，ctrl+alt+l 自动格式化代码   ctrl+alt+m 自动抽取方法  
数组名.fori 自动生成数组的索引遍历 ctrl+alt+t 代码包裹 ctrl+n 搜索并打开选择的类 ctrl+w选中一个单词
ctrl+b 跳转到光标所在的变量、类或方法的定义处 ctrl+f12 打开当前文件的结构视图 ctrl+alt+v 自动生成等式左边
alt+insert 自动生成标准Javab类(PTG插件)

## 基础知识
System.exit(0);  停止虚拟机的运行  
静态工厂方法 创建“新”对象的静态方法，如Interger.ValueOf()  
java中有3种移位运算符，<<带符号左移 >>带符号右移 >>>无符号右移  
浅拷贝：浅拷贝会在堆上创建一个新的对象（区别于引用拷贝的一点），不过，如果原对象内部的属性是引用类型的话，浅拷贝会直接复制内部对象的引用地址，也就是说拷贝对象和原对象共用同一个内部对象。  
深拷贝：深拷贝会完全复制整个对象，包括这个对象所包含的内部对象。
引用拷贝：引用拷贝就是两个不同的引用指向同一个对象

## 关键字
关键字字母全部小写
- break 结束循环或者 switch  
- continue 跳过循环的当前迭代执行下一轮迭代，只能用在循环中
- new 创建对象，在堆中分配内存空间；并返回对象的引用
- private 权限修饰符，被修饰的成员只能在本类中才能访问，缺省修饰符可以在包中的其他类中访问
- protected 权限修饰符，其他包中的子类也可以访问
- public 权限修饰符，所有的地方都可以访问
- this 区分成员变量和局部变量，代表方法调用者的地址值
- static 静态，修饰成员方法、成员变量，被该类所有对象共享，既可通过类名调用，也可使用对象名调用，不属于对象，属于类，随着类的加载而加载，优先于对象存在,静态方法不可访问非静态成员且没有this和super，static变量不会被序列化     
- super 父类存储空间  
- native 修饰方法，意味着该方法的实现不是由Java实现的，由外部代码提供实现
- instanceof 判断一个对象是一个类的实例  
- final 修饰方法、类、变量 不能被重写、继承，常量（只能被赋值一次）
- defaul 在接口中定义默认方法，或者在switch中只有default编写默认匹配情况
- strictfp 用于类、接口、方法中，表明方法中的浮点运算和数学函数的结果必须严格遵守IEEE 754标准，不受编译器优化影响及平台之间的差异性  
- synchronized 实现线程同步，会在执行时获得对象的锁，确保在同一时刻只有一个线程可以访问被锁定的代码块或方法  
- transient 修饰类的成员变量，表明不会被序列化，在对象写入流中时，该变量的值不会写入流中，从流中读取对象时，该变量的值会被初始化为默认值  
- volatile 修饰变量，始终保持可见性和顺序性，每次读取该变量的值都将从主内存中读取，每次写入该变量的值都将立即刷新到主内存中  
- assert 添加断言语句，检查程序中的错误和不变量，断言为False时终止程序的执行，运行程序时需要使用-ea参数

## 字面量
整数类型、小数类型、字符串类型、字符类型、布尔类型、空类型，字面量是常量   
long 类型的变量在数据值的后面需要加一个L作为后缀，float 类型的变量需要加一个F作为后缀    
空类型 null 不能直接打印，只能用字符串的形式 "null" 进行打印  
特殊字符：\t 打印的时候把前面字符串的长度补齐到8或者8的倍数，可以用来对齐打印内容  
&& 与 || 和 &、| 效果相同，但具有短路的效果，左边能确定整个表达式的结果，右边不执行

## 类型转换
基本数据类型：变量中存储的是真实的数据，整数、浮点数、字符、布尔，做形参时传递的是真实的数据，形参改变不影响实参的值  
引用数据类型：使用 new 创建对象 ，变量中存储的是地址值，类、接口、数组，做形参时传递的是地址值，形参改变影响实参的值   
### 隐式转换
取值范围小的转换成大的 byte < short < int < long < float < double
byte short char 三种类型的数据在数据运算时会自动转换成 int，再进行运算，char会通过 ASCII 转成对应数字进行运算  
### 强制转换
目标数据类型 变量名 = (目标数据类型) 被强转的数据;//可能发生失真  
if(a instanceof Dog d) 先判断再强转 等价于 if(a instanceof Dog){Dog d = (Dog)a}

## 包装类
把基本类型变成引用类型 
Integer<->int Long<->long Short<->short Float<->float Double<->double Character<->char Boolean<->boolean Byte<->byte  
包装类和基本数据类型可以互相转换，自动装箱拆箱（发生在编译阶段），装箱调用valueOf()方法，拆箱调用xxxValue()方法  
所有的包装类都是不变类，对象创建后不可变，不能使用==比较，需要使用equals()  
所有的整数和浮点数的包装类型都继承自Number，因此，可以非常方便地直接通过包装类型获取各种基本类型
```java
Integer n1 = new Integer(100);Integer n2 = Integer.valueOf(100);Integer n3 = Integer.valueOf("100");//推荐使用静态方法valueOf()
int i = Integer.parseInt("100");    //100 把字符串解析成一个整数
//"100",表示为10进制 "2s",表示为36进制 "64",表示为16进制 "144",表示为8进制 "1100100",表示为2进制，返回值都为String
Integer.toString(100) Integer.toString(100, 36) Integer.toHexString(100) Integer.toOctalString(100) Integer.toBinaryString(100)// 
Integer.bitCount(i)
Boolean.TRUE Boolean.FALSE
Integer.MAX_VALUE Integer.MIN_VALUE
Long.SIZE Long.BYTES// 64 (bits),8 (bytes)
Number num = new Integer(999); // 向上转型为Number
float f = num.floatValue(); // 获取float
byte x = -1;int ans = Byte.toUnsignedInt(x)  //255 有符号和无符号整型的转换
```

## 数组
```java
int[] arr; //数据类型[] 数组名     也可以 数据类型 数组名[]
int[] array = new int[]{1, 2, 3};   //静态初始化 可简写为 int[] array = {1, 2, 3}，初始化成功后数组长度不可变
int[] array = new int[5];           //动态初始化，由虚拟机给出默认的初始化值
int[] arr2 = arr;                  //共享同一个内存空间
arr.length;for(int i = 0; i < arr.length; i++)     //for(int num:nums)增强for
数据类型[][] 数组名 = new 数据类型[][] {{}, {}};   //二维数组初始化 数据类型[][] 数组名 = {{}, {}}; 数据类型[][] 数组名 = new 数据类型[m][n]
```

## 方法
方法重载：同一个类中，方法名相同，参数不同的方法，与返回值无关
可变长参数，只能作为方法的最后一个参数
```java
public  void func1() {}
public  void func2(int x, int y, ...){}
public  int func4(){return z;}
public  int func3(int x, int y){return x+y;}
public static void func5(String arg1, String... args) {}  //可变参数，底层是一个相应类型的数组
```

## 类
成员变量、成员方法、构造方法、代码块、内部类  
类名 对象名 = new 类名(); 对象名.成员变量; 对象名.方法名()  
Javabean类，描述一类事物的类，不写main方法  
测试类，带有main方法的类，是程序的入口  
工具类，不是用来描述一类事物的，而是帮我们做一些事情的类，私有化构造方法     
一个代码文件中可以定义多个类，但是只能一个类是public修饰的，public修饰的类名必须是Java代码的文件名称  
### 封装
把一个对象的状态信息（也就是属性）隐藏在对象内部，不允许外部对象直接访问对象的内部信息。但是可以提供一些可以被外界访问的方法来操作属性。  
如何正确的设计属性和方法：对象代表什么，就得封装对应的数据，并提供数据对应的行为，人开门，开门的方法应该定义在门这个类  
### 继承
当类与类之间，存在相同的内容，并满足子类是父类的一种，就可以考虑使用继承  
只支持单继承，不支持多继承，但支持多层继承，每一个类都直接或间接地继承Object，子类只能访问父类中非私有地成员  
可以把多个子类中重复的代码抽取到父类中，子类可以直接调用，减少代码冗余，提高代码的复用性  
虚方法表：非private、非static、非final，虚方法可以被继承  
构造方法、成员变量、成员方法  
### 多态
方法的重写：父类的方法不满足子类现在的需求时，需要进行方法重写 @Override ，覆盖虚方法表中的方法
重写方法的名称、形参列表必须与父类一致，访问权限子类必须大于等于父类，抛出的异常类子类必须小于等于父类，返回值类型子类必须小于等于父类，只有被添加到虚方法表中的方法才能被重写
同类型的对象，表项出不同的形态，有继承或实现关系；父类引用指向子类对象 父类类型 对象名称 = 子类对象;  有方法重写
定义方法的时候，使用父类型作为参数，可以接收所有子类对象  
调用成员变量，编译看左边，运行也看左边  
调用成员方法：编译看左边，运行看右边  
多态的弊端：不能调用子类的特有方法，解决方案：类型转换
### 构造方法
创建对象的时候，由虚拟机自动调用，给成员变量进行初始化  
方法名与类名相同，没有返回值类型但不能用void声明，无参构造和带参构造，没有定义构造方法，系统将给出一个默认的无参构造，如果定义了任意的构造方法，系统将不再提供默认的无参构造  
修饰符 类名(参数) {方法体;}  
支持重载，但不能重写
### 代码块
局部代码块 变量的作用域，提前结束变量的生命周期
构造代码块 在成员变量位置处的代码块，抽取构造方法中的重复部分，在变量创建前执行
静态代码块 static{}，在构造代码块前加static关键字，随着类的加载而加载，并且只执行一次 数据初始化
### 抽象类
抽取共性时，无法确定方法体，就把方法定义为抽象的，强制让子类按照某种格式重写
抽象方法：public abstract 返回值类型 方法名(参数列表);  
抽象类：public abstract class 类名 {}  
抽象类中不一定有抽象方法，但有抽象方法的类一定是抽象类，抽象类不能实例化，可以有构造方法  
抽象类的子类要么重写抽象类中的所有抽象方法，要么还是抽象类  
### 接口
一种规则，是对行为的抽象，如果一个接口里面没有抽象方法，则是一个标记性接口  
public interface 接口名 {}    public class 类名 implements 接口名 {}
接口不能实例化，接口和类之间是实现关系，通过implements表示，可以是多实现也可以在实现的同时继承一个类
接口和接口之间是继承关系，可以单继承，也可以多继承，如果实现可最下面的子接口，那么就需要重写所有的抽象方法
接口的实现类要么重写接口类中的所有抽象方法，要么是抽象类
接口中的成员变量只能是常量，默认修饰符public static final，没有构造方法  
接口中除了定义抽象方法，允许定义默认方法，使用default修饰：public default 返回值类型 方法名(参数列表) {}，以及静态方法：public static 返回值类型 方法名(参数列表) {} ，接口中的静态方法只能通过接口名调用，不能通过类和对象调用，私有方法，普通私有方法给默认方法服务和私有静态方法给静态方法服务，接口中的方法默认都是public访问修饰符
### 内部类
在一个类的里面再定义一个类，内部类表示的事物是外部类的一部分，单独出现没有任何意义
内部类可以直接访问外部类的成员，包括私有，外部类要访问内部类的成员，必须创建对象
成员内部类：写在成员位置的，属于外部类的成员，可以被修饰符所修饰，调用外部类的成员需要使用 外部类名.this.成员
静态内部类：使用static修饰的成员内部类，只能访问外部类中的静态变量和静态方法，如果想要访问非静态的需要创建对象
局部内部类：将内部类定义在方法里面，外界无法直接使用局部内部类，需要在方法内部创建对象并使用，该类可以直接访问外部类的成员，也可以访问方法内的局部变量
匿名内部类：隐藏了名字的内部类，new 类名或者接口名() {重写方法;}; 包含继承或实现、方法重写、创建对象，整体就是一个类的子类对象或者接口的实现类对象，当方法的参数是接口或者类时，但这个实现类只使用一次，就可以使用匿名内部类简化代码  

## string
```java
"jiang" + "xianqiang"  //jiangxianqiang，拼接字符串，3.7 + "abc" -> "3.7abc"，1 + 99 + "abc" -> "100abc"，拼接时如果没有变量参与，会进行编译优化，复用串池中的字符串
String name = "jxq";   //字符串的内容是不会发生改变的，创建后不可更改 直接赋值，字符串常量池，可以复用，==比较为true
String name = new String();                       //构造方法 String(String)、String(char[])、String(byte[])
String str = String.valueOf(obj)                  //obj.toString()
s1 == s2                    //基本数据类型比较的是值，引用数据类型比较的是地址值，new出来的地址值不一样，== 比较为false
s1.equals(s2) s1.equalsIgnoreCase(s2)  //比较字符串对象的内容是否相等，重写了Object的equals方法
s.length() s.charAt(i) s.substring(l, r) s.replace(old, new) s.startWith(str) s.repeat(3) 
String s1 = s.intern() //将指定的字符串对象引用保存在字符串常量池中，并返回该引用  
char[] arr = str.toCharArray(); byte[] byteArray = str.getBytes(); String[] strArray = str.split("");
StringBuilder sb = new StringBuilder()     //StringBuilder内容可变，StringBuilder(str) 扩容：默认容量16，新容量=老容量*2+2，如果不够则为目标容量，非线程安全
sb.append(任意类型) sb.reverse() sb.length() sb.toString() sb.charAt(0) sb.isEmpty() //链式编程sb.apppend(1).append(2).append(3)
StringJoiner sj = new StringJoiner(间隔符号)    //StringJoiner sj = new StringJoiner(间隔符号，开始符号，结束符号) 连接字符串
sj.add(添加内容) sj.length() sj.toString()
StringBuffer sb = new StringBuffer();sb.append("a".repeat(n - 1)).append("b").toString();  //线程安全
```

## 集合
集合不能直接存基本数据类型，需要存相应的包装类，自动扩容 
```java
import java.util.ArrayList;
ArrayList<String> list = new ArrayList<String>();                      //ArrayList<Integer> list = new ArrayList<>();
List<Integer> list = new ArrayList<Integer>();
list.add(e) list.remove(e) list.remove(i) list.set(i, e) list.get(i) list.size() 

PriorityQueue<int[]> pq = new PriorityQueue<int[]>((a, b) -> a[2] - b[2]); //小根堆，默认也是小根堆
pq.add(e);pq.offer(new int[]{0, i, f[0] + g[i]}); pq.isEmpty(); pq.poll();pq.peek();

Map HashMap TreeMap LinkedHashMap Entry
Map<String, String> map = new HashMap<>(); Map<List<Integer>, Integer> cnt = new HashMap<>();
put(key, value) get(key) remove(key) clear() containsKey(key) containsValue(value) isEmpty() size()//put会返回覆盖的值不存在则为null
merge(key, value, remappingFunction)     //map.merge(k, 1, Integer::sum)
Set<String> keys = map.KeySet()    //获取所有的键并放到Set中，通过map.get(key)遍历
for(String key: keys){System.out.println(key + "=" + map.get(key));}
Set<Map.Entry<String,String>> entries = map.entrySet()    //获取键值对对象的Set
for(Map.Entry<String,String> entry: entries){System.out.println(entry.getKey() + "=" + entry.getValue());}
map.forEach((key, value)-> System.out.println(key + "=" + value));
'''HashMap 键无序、不重复、无索引，哈希表，利用键计算哈希值，链表长度超过8且数组长度大于等于64转为红黑树，键位置如果存储的是自定义对象，需要重写hashCode和equals方法 '''
HashMap<String,String> hm = new HashMap<>();
'''LinkedHashMap 键有序（存储和取出的元素顺序一致）、不重复、无索引，底层数据结构依然是哈希表，只是每个键值对元素又额外多了一个双链表机制记录存储的顺序'''
LinkedHashMap<String, Integer> lhm = new LinkedHashMap<>();
'''TreeMap 红黑树结构，键不重复、无索引、可排序，默认按照键从小到大排序，也可以自定义键的排序规则：1.实现Comparable接口指定比较规则；2.传递Comparator比较器对象指定比较规则（第一种无法满足要求时，使用第二种），键是自定义对象时需要实现Comparable接口compareTo方法'''
TreeMap<Integer, String> tm = new TreeMap<>();
TreeMap<Integer, String> tm = new TreeMap<>(new Comparator<Integer>{
    @Override
    public int compare(Integer o1, Integer o2){
        //o1 当前要添加的元素 o2 已经在红黑树中的元素
        return o2 - o1;               //降序
    }
});

//of(E... elements) Set、Map类似，set中元素需要保证唯一性，map的键不能重复，且不可传递超过10个键值对
List<String> list = List.of("asd", "zxc", "qwe")   //不可变集合、
Map<Object, Object> map = Map.ofEntries(hm.entrySet().toArray(new Map.Entry[0])); //不可变map
Map<String, String> map = Map.copyOf(hm)  //jdk>=10，不可变map
```

## Scanner
```java
import java.util.Scanner;      //导包，放在类上面
Scanner sc = new Scanner(System.in);      //创建对象
int i = sc.nextInt();                     //接收数据 nextDouble()小数 next()字符串 遇到空格、制表符、回车就停止接收
String line = sc.nextLine()               //接收字符串 可以接收空格、制表符，遇到回车停止接收
```

## Random
```java
import java.util.Random;
Random r = new Random();
int num = r.nextInt(100) + 1;     // bound:100 0-99
```

## Math  工具类
```java
abs(int a) ceil(double a) floor(double a) round(float a) max(int a, int b) min(int a, int b) pow(double a, double b) random()
sqrt(double a) cbrt(double a)
```

## System 
```java
exit(int status) currentTimeMillis() arraycopy(源数组，起始索引，目的数组，起始索引，拷贝个数)
```

## Runtime
```java
getRuntime() exit(int status) availableProcessors() maxMemory() totalMemory() freeMemory() exec(String command)
```

## Object
```java
String toString() 返回对象的字符串表现形式 boolean equals(Object obj) 比较两个对象是否相等 int hashCode() 返回对象的哈希码
Object clone() 对象克隆，首先需要重写Object中的clone()方法，让Javabean类实现Cloneable接口，创建源对象并调用clone，浅拷贝，使用第三方gson可以深拷贝
Class<?> getClass() 返回当前运行对象的Class对象 void notify() void notifyAll() 唤醒线程 wait()暂停线程的执行 finalize() 对象被回收时触发的操作
```

## Objects 工具类
```java
equals(obj1, obj2)先做非空判断，再比较 isNull(obj) 判断对象是否为空 nonNull(obj)判断对象不为空
```

## BigInteger
对象一旦创建，内部的数据不能发生改变  
signum记录正负号 mag数组记录数据，32位分成一组，有理论上限
```java
BigInteger(int num, Random rnd) 随机大整数[0-2^num-1] BigInteger(String val)指定大整数 BigInteger(String val, int radix) 指定进制的大整数 //构造方法
BigInteger valueOf(long val) //静态方法获取BigInteger的对象，在long的取值范围之内，提前创建-16-16的BigInteger对象，不会多次创建
add(bi) subtract(bi) multiply(bi) divide(bi) divideAndRemainder(bi) equals(obj) pow(i) max(bi) intValue(bi)
```

## BigDecimal
用于小数的精确计算，表示很长的小数，不可变  
byte数组存储每一个字符对应的ascill值
```java
BigDecimal(String val) BigDecimal(double val) BigDecimal valueOf(double val)  //推荐使用String构造和静态valueOf
add(bd) subtract(bd) multiply(bd) divide(bd) divide(bd, 精确几位，舍入模式(RoundingMode类))//a.divide(b, 2, RoundingMode.HALF_UP)
compareTo(bd) setScale(3,RoundingMode.HALF_DOWN) equals(bd)  //equals会比较精度，而compareTo不会，推荐使用compareTo
```

## Arrays
```java 
toString(arr)      //把数组拼接成一个字符串
binarySearch(arr, num)    //数组元素必须是升序的，查找元素存在返回真实索引，不存在则返回-插入点-1
copyOf(arr, length)          //部分拷贝、完全拷贝、补上默认值
copyOfRange(arr, start, end)     //指定范围，包头不包尾
fill(arr, num)            //填充数组
sort(Integer[] arr, new Comparator<Integer>(){   //参数一待排数组，参数二排序规则
    @Override
    public int compare(Integer o1, Integer o2){   //o1待排元素，o2有序序列中的元素
        return o1-o2;                             //升序，o2-o1降序
    }
})     
sort(Integer[] arr, (Integer o1, Integer o2) -> {   //lambda表达式只能简化函数式接口的匿名内部类的书写
        return o1-o2;                               //函数式接口，有且仅有一个抽象方法的接口，接口上方可以加@FunctionalInterface
    }
)      
//lambda表达式省略规则
//1.参数类型省略不写
//2.如果只有一个参数，参数类型可以省略，同时()可以省略
//3.如果方法体只有一行，大括号、分号、return可以省略，且需要同时省略
sort(arr, (o1, o2) -> o1-o2)                            
```

## Collections 工具类
```java
addAll(Collection<T> c, T... elements) shuffle(List<T> list) sort(List<T> list) sort(List<T> list, Comparator<T> c)
binarySearch(List<T> list, T key) copy(List<T> dest, List<T> src) fill(List<T> list, T obj) max/min(Collection<T> c)
swap(List<T> list, int i, int j)
```

## Stream
Stream<T> stream 通常结合Lambda表达式简化集合、数组的操作
```java
list.stream()                           //获得单列集合的Stream流
hm.keySet().stream()                    //获得双列集合的键的Stream流
hm.entrySet().stream()                  //获得双列集合的键值对Stream流
Arrays.stream(arr)                      //获得数组的stream流
Stream.of("a", "b", "c")                //获得一堆相同类型零散数据的stream流 of(T... values)
//中间方法，返回新的Stream流，原来的Stream流只能使用一次，修改Stream流中的数据，不会影响原集合或者数组中的数据
list.stream().filter(s -> s < 1>)       //过滤，s是流中的每个元素
limit(long maxSize) skip(long n) distinct() //获取前几个元素 跳过前几个元素 去重（依赖hashCode和equals方法）
Stream.concat(Stream a, Stream b)     //合并流
map(Function<T, R> mapper) //转换流中的数据类型，T流中原本的数据类型，R要转成的数据类型
//终结方法
forEach(Consumer<? super T> action)         //遍历
list.stream().forEach(s -> System.out.println(s));
long count() //统计
String[] arr = list.stream().toArray(v -> new String[v]);  //v 流中数据的个数 创建对应类型的数组并返回装着流里面所有数据的数组
List<String> lst = list.stream().collect(Collectors.toList()) //收集到集合中，Collectors.toSet() 
list.stream().collect(Collectors.toMap(
                    s -> split("-")[0],
                    s -> Integer.parseInt(s.split("-")[2])));  //收集到map中，需指定键和值的生成规则，两个Function函数式接口，键不能重复
```

## 方法引用
把已经有的方法拿过来用当作函数式接口中抽象方法的方法体，简化Lambda表达式 ::方法引用符    
引用处必须是函数式接口  
被引用的必须已经存在，形参和返回值需要跟抽象方法保持一致，功能满足当前需求  
引用静态方法  类名::静态方法 list.stream().map(Integer::parseInt).forEach(s -> System.out.println(s));
引用成员方法  其他类对象::成员方法 this::成员方法 super::成员方法 this和super不能用在静态方法中  
引用构造方法  类名::new 用于创建对象，抽象方法的返回值应与创建的对象相同  
使用类名引用成员方法  类名::成员方法 被引用方法的形参应与抽象方法的第二个形参到最后一个形参保持一致，抽象方法的第一个形参表示被引用方法的调用者，决定了可以引用哪些类中的方法  
引用数组的构造方法 数据类型::new `Integer[] lst = list.stream().toArray(Integer[]::new);`  

## 异常
Error：系统级别的错误
Excepion：异常，程序可能出现的问题，查询Bug信息，作为方法内部的一种返回值，通知调用者底层的执行情况，从下往上看异常信息
运行时异常：RuntimeException本身及其子类，运行时出现
编译时异常：直接继承Exception，编译阶段就会错误提示，必须手动处理
```java
try{                                //捕获异常，可以让程序继续往下执行，没有异常发生则不会执行catch
    可能出现异常的代码               //出现异常，会创建异常对象，在catch中捕获这个异常，出现异常之后的代码不会执行
} catch(异常类名 变量名) {           //可以写多个catch与出现的异常匹配，父类异常写在下面，如果异常没有捕获，会交给jvm处理
    异常的处理代码                   //可以在一个catch中捕获多个异常，用 | 隔开，采取同一种处理方案
} finally {                         //不要咋finally代码块中使用return，finally只在线程死亡、cpu关闭、jvm关闭情况下不会执行
    代码块                          //无论是否捕获或处理异常，都会被执行。当在try或catch中遇到return时，将在方法返回之前被执行
}
try (ResourceType r1 = new ResourceType(); ResourceType r2 = new ResourceType();){} catch(Exception e) {}//try-with-resources语句
e.getMessage() e.toString() e.printStackTrace()  //返回throwable的详细消息字符串、返回异常的简短描述、把异常的错误信息输出在控制台
throw new RuntimeException();                 //写在方法内，结束方法，手动抛出异常交给调用者，之后的代码不再执行
public void func() throws 异常类名1, 异常类名2...{}   //写在方法定义处，声明一个异常，告诉调用者，使用本方法可能会有哪些异常，编译时异常必须要写，运行时异常可以不写
public class NewNameException extends RuntimeException {               //自定义异常
    public NewNameException() {}
    public NewNameException(String message) {super(message);}
}
```

## 反射
在运行时分析类以及执行类中方法的能力、动态代理
```java

```

## File
一个File对象就是一个路径
```java
File f = new File(String pathname) //创建file对象 File(String parent, String child) File(File parent, String child)
isDirectory() isFile() exists() 
length() getAbsolutePath() getPath() getName() lastModified()//length只能获取文件的大小，单位是字节，lastModified返回的是时间的毫秒值
createNewFile() mkdir() mkdirs() delete() //创建文件时会返回是否创建成功，如果路径不存在，会有IOException，只能删除文件或空文件夹
listFiles() //路径不存在、文件或需要权限才能访问的文件夹时返回null，空文件夹返回长度为0的数组
listRoots()  //静态方法，列出可用的文件系统根
list() list(FilenameFilter filter) listFiles(FilenameFilter filter) listFiles(FileFilter filter)
```