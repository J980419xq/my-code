```go
import _ "./hello"     //只是引用 hello 包，仅仅调用该包中的 init 函数，无法通过包名调用包中的其余函数
const mod int = 1e9 + 7                 //声明常量
sort.Slice(score, func(i, j int) bool { return score[i][k] > score[j][k] })      // i, j是切片索引
sort.Ints(coins)                          //从小到大排序 sort.Strings(ans)
left := sort.SearchInts(nums, target)    //二分，第一个大于等于target的下标
var dfs func(*TreeNode) string                             //lambda函数声明
find = func(root *TreeNode) *TreeNode{}
func swap(x, y string) (string, string) {                  //go函数可以返回多个返回值
   return y, x
}
var (                                      //批量声明变量
   a string
   b int
   c bool
   d float32
)
const (                                    //const 同时声明多个常量时，如果省略了值则表示和上面一行的值相同
   n1 = iota                               //0 iota 常量计数器 从该行开始，下一行的值为行索引值
   n2 = 100                                //100
   n3                                      //100
   n4 = iota                               //3
   n5                                      //4
)
defer func() { visited[x][y] = 0 }()  //defer用于资源的释放，会在函数返回之前进行调用
math.MaxInt
```

## 数组与切片 [...]int []int
```go
nums1 := [3]int{1,2,3,}     //数组，值传递 b := [...]int{2, 3, 5, 7, 11}未定大小数组的声明 var variable_name [SIZE]variable_type
nums2 := []int{1,2,3}       //切片，指针传递 ans := make([]int, 0, n) dist := make([][][2]int, n) make([]T, length, capacity)
nums3 := nums1[:]     ans = ans[:len(ans)-1]    //初始化切片nums3，是数组nums1的引用 左闭右开 slice := array[start:end+1:max] cap=max-start 浅拷贝,共享数组空间,超出数组cap，会划分新的底层数组
a := make([][]int, m) // 二维切片，m行
for i := range a {
   a[i] = make([]int, n) // 每一行n列
}
len(nums2) cap(nums2)       //切片的长度和容量
queue := [][3]int{{-1, -1, -1}}      //切片做队列
ans = append(ans, x)                 //切片添加元素，返回新切片对象        numbers = append(numbers, 2,3,4)
arr = append([]int{-1}, arr...)      //在前面添加元素
copy(numbers1,numbers)               //拷贝 numbers 的内容到 numbers1 要初始化numbers1的 size (深拷贝)
```

## map与set、heap
```go
type pair struct{ l, r int }
m := map[int]pair{}        m[0] = pair{-1, -1}
seen := map[string]*TreeNode{}       //初始化 make(map[string]*TreeNode【, cap】)
if n, ok := seen[temp]; !ok {}        //map查找
for node := range repeat             //set遍历 range可用于切片、数组、map、字符串  for i,x:= range numbers
curSet := map[string]struct{}{s: {}} nextSet[str[:i]+str[i+1:]] = struct{}{}
delete(countryCapitalMap, "France")  //delete(map,key)

func (pq PriorityQueue) Len() int {
    return len(pq)
}
func (pq PriorityQueue) Less(i, j int) bool {
    return pq[i][0] > pq[j][0]
}
func (pq PriorityQueue) Swap(i, j int) {
    pq[i], pq[j] = pq[j], pq[i]
}
func (pq *PriorityQueue) Push(x interface{}) {
    item := x.([]int)
    *pq = append(*pq, item)
}
func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    item := old[n-1]
    *pq = old[:n-1]
    return item
}


```

## string byte rune
```go
func (c Celsius) String() string    { return fmt.Sprintf("%g°C", c) }   //进行格式化 %v 输出时会自动调用该类型的String()方法
strings.Contains("aeiou", w[:1])    //包含
strings.HasPrefix(str1, str2)       //前缀 strings.HasSuffix() 后缀
strings.IndexByte(s, '0')           //查找字符索引
strings.Index(s, str)               //在 s 中查找 str 并返回第一个字符的索引，或者返回-1
strings.LastIndex(s, str)
strings.Repeat("-",3)               //"---",重复字符串
strings.Join(os.Args[1:], " ")      //连接字符串
strings.Split(s string, sep string) //切割字符串，返回子字符串切片
strings.FieldsFunc(s string,  f func(rune) bool) //返回字符串切片
bytes.Count(suits, suits[:1])       //[]byte
for _, c := range s {}  //c为 rune类型， 需要使用byte(c)转化为byte类型，使用下标就为 byte 类型
//string只读，需要通过byte[]或rune[]转换进行修改
var ans []byte // string(ans) ans = append(ans, '%', '2', '0')  b := []byte(s) 
serial := fmt.Sprintf("%d(%s)(%s)", node.Val, dfs(node.Left), dfs(node.Right)) //拼接字符串 也可以用"+"
aStr := "100"
bInt, err := strconv.Atoi(aStr)    //string to int
cInt := 200
dStr := strconv.Itoa(cInt)         //int to string
binaryStr := strconv.FormatInt(int64(num), 2) //num 转换成二进制字符串表示
num,err := strconv.ParseInt(binaryStr, 2, 0) //将二进制表示转换成整数
unicode.IsDigit(rune(s[pos]))      //判断数字字符
str2 := `this is another           
string`                            //多行字符串
var sb strings.Builder              //字符串生成器，结构体类型
sb.String()                         //将 sb 对象转换成 string 类型
sb.Len() sb.Cap() sb.Reset()        //长度、容量、重置
sb.Grow(n int)                      //增加容量，可能会重新分配底层数组
sb.Write(p []byte)                  //追加字符切片，返回 p 的长度和 err
sb.WriteRune(r rune)                //追加 Unicode 类型字符，返回写入的字节数和 err
sb.WriteString(s string)            //追加字符串，返回字符串长度和 err
sb.WriteByte(c byte)                //追加字符，返回 err
```

## 结构体
```go
var node *Node                  //初始化结构体指针
node := &Node{Val: -1}          //对象初始化，指针传递，结构体指针的访问属性时无需加*
type Books struct {             //type struct_variable_type struct {
   title string                 //  member definition
   author string                //  member definition
   subject string               //  ...
   book_id int                  //  member definition
   mp  map[string]int
   group map[int][]int
}                               //}
func Constructor() Books {
    return Books{map[int]int{}, map[int][]int{}, 0}
}
Books{"Go 语言", "www.runoob.com", "Go 语言教程", 6495407} //variable_name := structure_variable_type {value1, value2...valuen}或者variable_name := structure_variable_type { key1: value1, key2: value2..., keyn: valuen}
Book1.title                     //结构体.成员名访问成员
```

## 接口
把所有的具有共性的方法定义在一起，任何其他类型只要实现了这些方法就是实现了这个接口
go没有类的概念，不存在传统意义上的继承，需要通过结构体组合和接口实现继承
```go
type interface_name interface {
   method_name1 [return_type]
   method_name2 [return_type]
   method_name3 [return_type]
   ...
   method_namen [return_type]
}
```

## 反射
在运行时动态的获取和操作程序的结构信息，例如变量的类型、值、方法等  
```go
var t reflect.Type                               //接口，一个go类型
t = reflect.TypeOf(i interface{})                //接受interface{} 类型, 并以reflect.Type形式返回其动态类型
var v reflect.Value                              //装载任意类型的值
v = reflect.ValueOf(i interface{})               //接受interface{} 类型, 并返回一个装载着其动态值的reflect.Value
t = v.Type()                                     //返回 reflect.Value 类型所对应的reflect.Type
x := v.Interface()                               //reflect.ValueOf()的逆操作，返回一个interface{} 类型，装载着与reflect.Value 相同的具体值
v.Kind()                                         //返回 reflect.Value 类型的基础类型, reflect.String、reflect.Int等
p := Person{Name: "jxq", Age: 25}
v = reflect.ValueOf(p)
v.NumField()                                     //返回结构体类型的字段数量
v.Field(i int)                                   //返回结构体类型第 i 个字段的值，reflect.Type 同样适用 reflect.TypeOf(p).Field(i).Name
v.NumMethod()                                    //返回结构体类型的方法数量
v.Method(i).Type()                               //返回结构体类型的第 i 个方法的类型
v.Elem()                                         //返回指针类型所指向的值或接口类型包含的值
v.Set()                                          //设置一个类型的值为新值，这个值必须为可修改的，通常为指针类型的Elem()
```

## 同步原语
```go
sync.Mutex.Lock()                                //互斥锁加锁
sync.Mutex.Unlock()                              //互斥锁解锁
sync.RWMutex.Lock()                              //获取写锁
sync.RWMutex.UnLock()                            //释放写锁
sync.RWMutex.RLock()                             //获取读锁
sync.RWMutex.RUnLock()                           //释放读锁
var wg sync.WaitGroup                            //等待一组 goroutine 返回，本质是一个计数器，wg := &sync.WaitGroup{}
wg.Add(i int)                                    //将计数器的值增加指定的数量 i
wg.Wait()                                        //等待计数器的值变为0，即等待一组 goroutine 的执行
wg.Done()                                        //将计数器的值减1
var o sync.Once                                  //保证在 Go 程序运行期间某段代码只会执行一次 o := &sync.Once{}
o.Do(f func())                                   //接收一个入参为空的函数，保证该函数只执行一次，函数不同也只会执行第一个
c := sync.NewCond(l sync.Locker)                 //返回 *sync.cond，让一组 Goroutine 都在满足特定条件时被唤醒，初始化时需要传入一个互斥锁                                   
c.Wait()                                         //使当前 goroutine 陷入休眠，等待条件变量的发生，调用前一定要使用锁
c.Broadcast()                                    //通知所有等待的 goroutine 条件变量的发生，并唤醒所有等待的 goroutine
c.Signal()                                       //通知等待的 goroutine 条件变量的发生，并唤醒其中一个等待的 goroutine
var m sync.Map                                   //map 不是并发安全的，m := sync.Map{} var m *sync.Map = &sync.Map{}
m.Store(key, value)                              //写入键值对
m.Load(key)                                      //读取键值对，返回 (value any, ok bool)
m.LoadOrStore(key, value )                       //key 不存在时，写入 value，否则返回已存在的 value，返回(value any, loaded bool)
m.Delete(key)                                    //删除键值对，返回(value any, loaded bool) 
m.Range(f)                                       //遍历键值对，f 的函数签名为 func(key, value any) bool
//原子操作见飞书
```
扩展原语golang.org/x/sync/semaphore   
```go
var g errgroup.Group                             //在一组 goroutine 中提供同步、错误传播以及上下文取消的功能 g := &errgroup.Group{}
g.Go(f func() error)                             //创建一个 goroutine 并执行传入的函数
g.Wait()                                         //等待所有 goroutine 返回，若返回错误则这一组 goroutine 最少返回一个错误
sem := semaphore.NewWeighted(i int64)            //创建指定权重的信号量，返回 *Weighted
sem.Acquire(ctx Context, n int64)                //阻塞获取指定权重的资源，如果没有空闲资源，会陷入休眠等等，上下文参数为信号量的获取设置超时时间
sem.TryAcquire(n int64)                          //非阻塞获取指定权重的资源，如果没有空闲资源，直接返回false
sem.Release(n int64)                             //释放指定权重的资源
var sfg singleflight.Group                        //避免重复的计算或者网络请求  g := &singleflight.Group{}
sfg.Do(key string, fn func() (interface{}, error)) //同步阻塞调用传入的函数
sfg.DoChan(key string, fn func() (interface{}, error)) //异步调用传入的参数并通过 Channel 接收函数的返回值
sfg.Forget(key string)                            //在持有的映射表中删除某个键，接下来对该键的调用就不会等待前面的函数返回
```

### time
```go
time.Sleep(time.Second)                  //延时
time.Duration()
timer := time.NewTimer(2 * time.Second)  //创建一个持续时间为指定值的定时器 timer ，只会发送一次超时信号，适合一次执行任务
<-timer.C                                //定时器的超时通道，超时后，会将当前时间发送给该通道
<-time.After(2 * time.Second)            //超时后，通过超时通道返回当前时间
timer.Stop()                             //关闭定时器，定时器已经关闭或者到期则 false
timer.Reset(1 * time.Second)             //重置定时器，定时器已经关闭或者到期则 false
ticker := time.NewTicker(2 * time.Second)//定时器 ticker 周期性地触发超时信号，适合周期性执行任务
```

### math
```go
math.MinInt math.MaxFloat64
math.Max(x, y float64) float64   math.Min(x, y)
```