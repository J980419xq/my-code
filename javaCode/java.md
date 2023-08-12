## idea快捷键
shift+shift 打开搜索框，全局搜索  
alt+enter 快速修复  
shift+F10 运行代码， shift+F9 debug代码，ctrl+F8 设置断点    
psvm 快捷键生成 main 函数，sout 输出语句 ctrl+p 提示构造方法属性 ctrl+alt+b 跳转到方法实现处
ctrl+/ 单行注释， ctrl+shift+/ 多行注释，ctrl+alt+l 自动格式化代码   ctrl+alt+m 自动抽取方法  
数组名.fori 自动生成数组的索引遍历 集合.for 自动生成增强for遍历 ctrl+alt+t 代码包裹 ctrl+n 搜索并打开选择的类 ctrl+w选中一个单词
ctrl+b 跳转到光标所在的变量、类或方法的定义处 ctrl+f12 打开当前文件的结构视图 ctrl+alt+v 自动生成等式左边 ctrl+d 向下复制一行
alt+insert 自动生成标准Javab类(PTG插件)

## 基础知识
System.exit(0);  停止虚拟机的运行  
静态工厂方法 创建“新”对象的静态方法，如Interger.ValueOf()  
java中有3种移位运算符，<<带符号左移 >>带符号右移 >>>无符号右移  
浅拷贝：浅拷贝会在堆上创建一个新的对象（区别于引用拷贝的一点），不过，如果原对象内部的属性是引用类型的话，浅拷贝会直接复制内部对象的引用地址，也就是说拷贝对象和原对象共用同一个内部对象。  
深拷贝：深拷贝会完全复制整个对象，包括这个对象所包含的内部对象。
引用拷贝：引用拷贝就是两个不同的引用指向同一个对象  
泛型：1.统一数据类型2.把运行期的问题提前到了编译期，避免强制类型转换出现的异常，在编译阶段确定数据类型  
不写泛型默认是Object类型，泛型可以在类、方法、接口中定义 <E> 类名后、方法修饰符后、接口名后  
泛型通配符? 一切类型 ? extends E 可以传递E或者E所有子类类型  ? super E 可以传递E或者E所有父类类型 <? extends E>

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
Integer.MAX_VALUE Integer.MIN_VALUE
Boolean.TRUE Boolean.FALSE
Long.SIZE Long.BYTES// 64 (bits),8 (bytes)
Character.isDigit(char c)
Number num = new Integer(999); // 向上转型为Number
float f = num.floatValue(); // 获取float intValue()
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
支持重载，但不能重写，不会被继承，想要使用父类的构造方法需要使用super关键字
### 代码块
局部代码块 变量的作用域，提前结束变量的生命周期
构造代码块 在成员变量位置处的代码块，抽取构造方法中的重复部分，在变量创建前执行
静态代码块 static{}，在构造代码块前加static关键字，随着类的加载而加载，并且只执行一次 数据初始化
同步代码块 synchronized(obj) {} 把操作共享数据的代码锁起来，锁对象obj一定是要唯一的，使用static修饰或使用当前类的字节码文件对象
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
在一个类的里面再定义一个类，内部类表示的事物是外部类的一部分，依赖外部类而存在，单独出现没有任何意义，而且又是一个独立的个体  
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
s.length() s.charAt(i) s.substring(l, r) s.replace(old, new) s.startWith(str) s.repeat(3) s.compareTo(s2)
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
Collection List Set ArrayList LinkedList Vector HashSet TreeSet LinkedHashSet           //单列集合
add(E e) clear() remove(E e) contains(Object obj) isEmpty() size() addAll(Collection<? extends E> c) removeAll(Collection<?> c) //contains底层依赖equals判断是否存在
toArray(T[] a)   //将集合转成对应类型的数组
Collection<String> coll = new ArrayList<>();
Iterator<String> it = coll.iterator(); while(it.hashNext()){sout(it.next());}//迭代器遍历时不能用集合的方法进行增删，hasNext判断当前位置是否有元素 next获取当前元素并移动指针
it.remove()          //迭代器遍历时可以用来进行删除  迭代器是在集合底层创建了一个内部类对象，遍历时会校验集合变化的次数modCount
for(String s:coll){sout(s);}            //增强for遍历，单列集合或数组 修改增强for中的变量不会改变集合中原本的数据
coll.forEach(new Consumer<String>(){               //forEach 匿名内部类或者Lamnbda表达式进行遍历 底层使用普通for进行遍历
    @override                                      //coll.forEach(s -> sout(s));
    public void accept(String s){
        sout(s);
    }
});
//List接口 存取元素有序、可重复、有索引
List<Integer> list = new ArrayList<Integer>();
list.remove(i) list.set(i, e) list.get(i)  list.add(i, e) for(int i = 0; i < list.size(); i++) {sout(list.get(i));} //list可以使用索引增删改查及遍历 set会返回被修改的元素
ListIterator<String> it = list.listIterator(); it.add(str)     //列表迭代器，增加了add方法以及反向遍历
ArrayList<String> al = new ArrayList<>();         //Object[]数组，空参创建时底层会创建一个长度为0的数组，添加第一个元素时创建一个长度为10的新数组，存满时扩容1.5倍   
al.addAll(list1)  //一次性添加多个元素时，1.5倍放不下，以实际长度为准
LinkedList<String> ll = new LinkedList<>();        //双向链表 内部有一个Node内部类
addFirst(E e) addLast(E e) getFirst() getLast() removeFirst() removeLast()  //实现了双端队列接口
Vector                                               //Object[]数组 相比ArrayList线程安全，已被淘汰
//Queue接口
Queue<int[]> q = new ArrayDeque<>();
q.offer(new int[]{i, j}) q.poll() q.peek() // 与add(E e) remove() element()区别在于不返回异常而是返回特殊值
ArrayQueue<int[]> dq = new ArrayDeque<>();                                 //双端队列  Object[]数组+双指针
offerFirst(E e) offerLast(E e) pollFirst() pollLast() peekFirst() peekLast() push() pop()     //同样可以模拟栈
PriorityQueue<int[]> pq = new PriorityQueue<int[]>((a, b) -> a[2] - b[2]); //小根堆，默认也是小根堆 Object[]数组实现二叉堆
//Set接口 存取元素无序、不重复、无索引
Set<String> set = new HashSet<>();
HashSet<String> hs = new HashSet<>();           //无序、不重复、无索引 哈希表（数组+链表+红黑树）装载因子大于0.75时数组两倍扩容、链表长度超过8且数组长度大于等于64转换为红黑树
LinkedHashSet<String> lhs = new LinkedHashSet<>();      //存取有序、不重复、无索引 通过双向链表记录元素存储的顺序
TreeSet<String> ts = new TreeSet<>();                  //可排序、不重复、无索引 红黑树 默认从小到大排序 自定义对象1.实现Comparable接口2.传递Comparator比较器对象，优先选1
//双列集合
Map HashMap TreeMap LinkedHashMap Entry
Map<String, String> map = new HashMap<>(); Map<List<Integer>, Integer> cnt = new HashMap<>();
put(key, value) get(key) remove(key) clear() containsKey(key) containsValue(value) isEmpty() size()//put会返回覆盖的值不存在则为null
map.computeIfAbsent(k, k -> new PriorityQueue<>()).offer(1);     //返回value对象的引用，如果key不存在则会创建一个默认value与key进行关联
merge(key, value, remappingFunction)     //map.merge(k, 1, Integer::sum)
Set<String> keys = map.KeySet()    //获取所有的键并放到Set中，通过map.get(key)遍历
for(String key: keys){System.out.println(key + "=" + map.get(key));}
Set<Map.Entry<String,String>> entries = map.entrySet()    //获取键值对对象的Set
for(Map.Entry<String,String> entry: entries){System.out.println(entry.getKey() + "=" + entry.getValue());}
map.forEach((key, value)-> System.out.println(key + "=" + value));
Iterator<Map.Entry<Integer, String>> iterator = map.entrySet().iterator();
'''HashMap 键无序、不重复、无索引，哈希表，利用键计算哈希值，键位置如果存储的是自定义对象，需要重写hashCode和equals方法 '''
HashMap<String,String> hm = new HashMap<>();  //默认初始化大小为 16。装载因子大于0.75时数组两倍扩容、链表长度超过8且数组长度大于等于64将链表转换为红黑树
'''LinkedHashMap 键有序（存储和取出的元素顺序一致）、不重复、无索引，底层数据结构依然是哈希表，只是每个键值对元素又额外多了一个双链表机制记录存储的顺序'''
LinkedHashMap<String, Integer> lhm = new LinkedHashMap<>();
'''TreeMap 红黑树结构，键不重复、无索引、可排序，默认按照键从小到大排序，也可以自定义键的排序规则：1.实现Comparable接口compareTo方法；2.传递Comparator比较器对象指定compare规则（第一种无法满足要求时，使用第二种）'''
TreeMap<Integer, String> tm = new TreeMap<>();
TreeMap<Integer, String> tm = new TreeMap<>(new Comparator<Integer>{               //new TreeMap<>((o1, o2) -> o1 - o2);
    @Override
    public int compare(Integer o1, Integer o2){
        //o1 当前要添加的元素 o2 已经在红黑树中的元素 compareTo方法中this是o1，参数o是o2
        return o2 - o1;               //降序     返回值小于0 o1存左边 等于0 不存 大于0 存右边
    }
});
//of(E... elements) Set、Map类似，set中元素需要保证唯一性，map的键不能重复，且不可传递超过10个键值对
List<String> list = List.of("asd", "zxc", "qwe")   //不可变集合、
Map<Object, Object> map = Map.ofEntries(hm.entrySet().toArray(new Map.Entry[0])); //不可变map
Map<String, String> map = Map.copyOf(hm)  //jdk>=10，不可变map
//并发集合类
ConcurrentHashMap
CopyOnWriteArrayList
ArrayBlockingQueue            //有界，需要指定容量
LinkedBlockingQueue           //无界
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
所有类的父类
```java
//自定义javabean最好重写equals和hashCode方法 Obeject的equals和hashCode默认用地址值进行计算，推荐根据对象属性值进行重写，发生哈希碰撞时使用equals进行比较是否相等
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

## Arrays  数组Array的工具类
```java 
toString(arr)      //把数组拼接成一个字符串
binarySearch(arr, num)    //数组元素必须是升序的，查找元素存在返回真实索引，不存在则返回-插入点-1
copyOf(arr, length) copyOfRange(arr, start, end)    //部分拷贝、完全拷贝、补上默认值    指定范围，包头不包尾
Arrays.asList(T... a)     //将数组转成对应类型的List，不能是基本类型可以是二维的基本数据类型数组，且返回的list不能使用修改list的add/remove/clear方法 List list = new ArrayList<>(Arrays.asList("a", "b", "c"))
fill(arr, num)            //填充数组
sort(Integer[] arr, new Comparator<Integer>(){   //参数一待排数组，参数二排序规则，自定义Comparator只支持引用类型
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

## Collections 集合工具类
```java
addAll(Collection<T> c, T... elements) shuffle(List<T> list) sort(List<T> list) sort(List<T> list, Comparator<T> c) reverse(List list) swap(List list, int i , int j) emptyList()
binarySearch(List<T> list, T key)   max/min(Collection<T> c) frequency(Collection c, Object o) replaceAll(List list, Object oldVal, Object newVal)
rotate(List list, int distance) fill(List<T> list, T obj) copy(List<T> dest, List<T> src) indexOfSubList(List list, List target) 
```

## Stream
Stream<T> stream 通常结合Lambda表达式简化集合、数组的操作，不可以是基本数据类型，基本数据类型有对应的流如IntStream
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
map(Function<T, R> mapper) //转换流中的数据类型，T流中原本的数据类型，R要转成的数据类型，不可以是基本数据类型，基本数据类型需要使用mapToXXX
mapToInt() sorted() boxed() //拆箱 排序 装箱
//终结方法
forEach(Consumer<? super T> action)         //遍历
list.stream().forEach(s -> System.out.println(s));
long count() //统计
String[] arr = list.stream().toArray(v -> new String[v]);  //v 流中数据的个数 创建对应类型的数组并返回装着流里面所有数据的数组
List<String> lst = list.stream().collect(Collectors.toList()) //收集到集合中，Collectors.toSet() 
list.stream().collect(Collectors.toMap(                 //value不可为空指针
                    s -> split("-")[0],
                    s -> Integer.parseInt(s.split("-")[2]),
                    (k1, k2) -> k1))  //收集到map中，需指定键和值的生成规则，两个Function函数式接口，第三个参数指定key冲突后的处理
list.stream().findFirst()      //返回流中第一个值包装后的Optional对象
```

## Optional
包装器类 存的值为任意类型，判断值为null时才使用Optional类
```java
Optional<String> empty = Optional.empty();    //返回空的Optional对象 
Optional<String> opt = Optional.of(String str);   //返回非空值Optional对象，参数不可为空
Optional<String> opt = Optional.ofNullable(name());  //返回特定值的Optional对象，参数为空则返回空的Optional对象
opt.isPresent()    //判断是否不为空Optional对象
opt.isEmpty()     //判断是否为空的Optional对象
opt.isPresent(s -> sout(s));   //如果不为空Optional对象，存的值调用Consumer接口实现的方法
opt.get()     //返回Optional存的值，如果为null则报异常
opt.orElse(String default) //返回Optional存的值，如果为null则返回默认值，默认值如果是方法返回值，虽然不一定用到但还是会创建
opt.orElseGet(() -> "yyh") //返回Optional存的值，如果为null则调用Supplier接口实现的方法，方法可能不会调用比orElse节省成本
opt.orElseThrow(() -> new Throwable("出错啦"))   //如果值为null会抛出Supplier接口定义的异常
opt.filter(o -> o.equals("yyh")) //过滤Optional，如果存的值不为null且符合Predicate接口实现的规则返回该Optional，否则返回空Optional对象
opt.map(o -> Integer.parseInt(o))               //转换Optional值的类型，值调用Function接口的实现方法进行转换，返回新Optional对象
opt.flatMap()            //与map区别在于Function接口apply方法返回值不一样，直接返回apply的返回值，map会对apply的返回值使用Optional包装
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
在运行时分析类以及执行类中方法的能力、动态代理、idea的代码提示
反射允许对封装类的字段，方法和构造函数的信息进行编程访问
作用：1.获取一个类里面的所有信息，获取到了之后，再执行其他业务逻辑；2.结合配置文件，动态的创建对象并调用方法
动态代理：无侵入式的给代码增加额外的功能，通过代理转移部分对象的功能，对象有什么方法想要被代理，代理就一定要有对应的方法，通过接口实现    
```java
Class.forName("全类名") 类名.class 对象.getClass()   //获取Class对象的三种方式
Class clazz = Class.forName("day2023617.HelloWorld");
getConstructors() getDeclaredConstructors() getConstructor(Class<?>... parameterTypes) getDeclaredConstructor(Class<?>... parameters)    //获取Class对象的构造方法Constructor，可以通过Constructor获取名字、权限修饰符、形参、构造对象
Constructor con = clazz.getConstructor(String.class);
con.getModifiers() con.getParameters() con.newInstance(Object... initargs) con.setAccessible(true)
getFields() getDeclaredFields() getField(String name) getDeclaredField(String name) //获取Class对象的成员变量Field，获取权限修饰符、名字、成员变量数据类型、对象成员变量记录的值，修改成员变量的值
Field field = clazz.getFields(name);
field.getModifiers() field.getName() field.getType() field.get(obj) field.setAccessible() field.set(obj, Object value)
getMethods() getDeclaredMethods() getMethod(String name, Class<?>... parameterTypes) getDeclaredMethod(String name, Class<?>...parameterTypes) //获取Class对象的成员方法Method，获取修饰符、名字、形参、返回值、方法抛出的异常，运行方法
Method method = clazz.getDeclaredMethod("setName", String.class) 
method.getParameters() m.getExceptionTypes() m.invoke(obj, Objectr... args)
Object obj = Proxy.newProxyInstance(ClassLoader loader, Class<?>[] interfaces, InvocationHandler h);
```

## File
一个File对象就是一个文件或者文件夹的路径
```java
File f = new File(String pathname) //创建file对象 File(String parent, String child) File(File parent, String child)
isDirectory() isFile() exists() 
length() getAbsolutePath() getPath() getName() lastModified()//length只能获取文件的大小，单位是字节，lastModified返回的是时间的毫秒值
createNewFile() mkdir() mkdirs() delete() //创建文件时会返回是否创建成功，如果路径不存在，会有IOException，只能删除文件或空文件夹
listFiles() //路径不存在、文件或需要权限才能访问的文件夹时返回null，空文件夹返回长度为0的数组
listRoots()  //静态方法，列出可用的文件系统根
list() list(FilenameFilter filter) listFiles(FilenameFilter filter) listFiles(FileFilter filter)
```

## I/O流
用于读写文件或者网络中的数据
流的方向：输入流和输出流
操作文件类型：字节流（所有类型文件）和字符流（纯文本文件）
```java
//InputStream 字节输入流
FileInputStream fis = new FileInputStream(File f);   //如果文件不存在，直接报错
fis.read() fis.read(byte[] b)  fis.close()       //一次读一个字节，读数据时返回的是数据在ASCII上对应的数字，读到文件末尾，返回-1，使用char强转
BufferedInputStream bis =  new BufferedInputStream(new FileInputStream(File f), int size)  //包装了基本字节输入流，增加了缓冲区，默认8192字节数组
//OutputStream 字节输出流
FileOutputStream fos = new FileOutputStream(File f, boolean append);  //创建本地文件字节输出流对象，如果文件不存在会创建一个新文件，但需要保证父级路径存在，如果文件存在会清空文件
fos.write(int b)fos.write(byte[] b, int off, int len) fos.close() //写数据时使用ASCII字符 fos.write(str.getBytes()) 想要换行就写入换行符
BufferedOutputStream bos =  new BufferedOutputStream(new FileOutputStream(File f), int size)  //包装了基本字节输出流，增加了缓冲区，默认8192字节数组
//字符流 = 字节流 + 字符集
//字符输入流 
FileReader fr = new FileReader(File f); //会关联文件并创建长度为8192字节的数组缓冲区 FileReader(String fileName, Charset charset)指定字符编码
read() read(char[] buffer, int off, int len)  //默认一次读一个字节，遇到中文会一次读多个字节，返回字符集上的数字，使用char强转，有参read会把读取到的数据存到数组中
BufferedReader br = new BufferedReader(Reader r)
br.readLine()              //读取一行数据，如果没有数据可读返回null
//字符输出流
FileWriter fw = new FileWriter(File f, boolean append);   //也会创建8192字节数组的缓冲区
write(int c) write(String str, int off, int len) write(char[] cbuf, int off, int len) flush()
BufferedWriter bw = new BufferedWriter(Writer w)
bw.newLine()
InputStreamReader isr = new InputStreamReader(InputStream is, String charsetName);  //转换流，将字节流转成字符流，可以指定字符编码
OutputStreamWriter osw = new OutputStreamWriter(OutputStream os, String charsetName);
ObjectInputStream ois = new ObjectInputStream(InputStream in);   //反序列化流，将文件中的对象读到程序中
ois.readObject()
ObjectOutputStream oos = new ObjectOutputStream(OutputStream out);        //序列化流，把对象写到文件中，需要实现序列化接口（无方法，标记型接口），序列化对象注意指定版本号 serialVersioUID
oos.write(Object obj)
PrintStream(OutputStream o) PrintStream(String fileName, Charset c)            //字节打印流，只能输出
write(int b) println(XXX xxx) print(XXX xxx) printf(String format, Object... args)
PrintWriter(Write w, boolean autoFlush)           //字符打印流，存在缓冲区，开启自动刷新
ZipInputStream zip = new ZipInputStream(new FileInputStream(File src));    //解压缩流，将压缩包文件作为输入
ZipEntry entry = zip.getNextEntry();             //获取压缩包中的每一个ZipEntry对象即文件或文件夹
ZipOutputStream zos = new ZipOutputStream(new FileOutputStream(dest, "a.zip"));  //压缩流
ZipEntry entry = new ZipEntry(String name);    //创建ZipEntry对象，
zos.putNextEntry(entry);                    //将ZipEntry对象放入压缩包中
zos.write(int b)                        //读取文件数据到压缩包中
```

## Thread
```java
thread.setName(thread.getName()) thread.start() thread.setPriority(thread.getPriority()) thread.setDaemon(boolean on)
Thread.currentThread() Thread.sleep(long time) Thread.yield() Thread.join()
```

## 网络编程
```java
// InetAddress IP类 子类 Inet4Address Inet6Addesss
static InetAddress getByName(String host) //构造方法私有，需要使用静态方法获取主机ip，
String getHostName() String getHostAddress()
// UDP
DatagramSocket ds = new DatagramSocket();  //创建socket，空参构造使绑定随机端口
DatagramPacket dp = new DatagramPacket(byte[] buf, int offset, int length, InetAddress address, int port) //UDP数据报
ds.send(dp) ds.close()
ds.receive(dp) dp.getData() dp.getLength() dp.getAddress() dp.getPort() ds.close()
MulticastSocket ms = new MulticastSocket(int port) //组播socket
InetAddress address = InetAddress.getByname("224.0.0.1");
ms.joinGroup(address)    //将本机加入224.0.0.1组播中
// TCP
Socket socket = new Socket(String host, int port) //客户端，需要指定服务端host，连接失败报错
OutputStream os = socket.getOutputStream();
os.write(byte[] buf)
ServeSocket ss = new ServeSocket(int port);//服务端
Socket socket = ss.accept();
InputStream is = socket.getInputStream();
is.read()
```

## Guava
```java
//可变集合
List<String> l1 = Lists.newArrayList(anotherListOrCollection);    // from collection
List<String> l2 = Lists.newArrayList(aStringArray);               // from array
List<String> l3 = Lists.newArrayList("or", "string", "elements"); // from varargs
List<String> l4 = Lists.newArrayList();                           //empty list
Maps.newConcurrentMap()
Maps.newHashMap()
//不可变集合
List<String> il = ImmutableList.of("string", "elements");  // from varargs
List<String> il = ImmutableList.copyOf(aStringArray);      // from array
```