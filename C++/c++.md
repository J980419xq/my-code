$n^2$
#include<bits/stdc++.h>
```bash
g++ hello.cpp -o hello;
g++ f1.cpp f2.cpp -o myexec
```
## 常见函数
```c++
//基于范围的for循环
vector<int>nums={2,4,6};
for(int &x:nums){                      //使用&可修改x
    x++;
}                
for(int x:nums){                       //不使用&，不可修改x
    cout<<x<<" ";
}
for (const auto &row : ia)             // for every element in the outer array 外层循环控制变量必须声明成引用类型
    for (auto col : row)               // for every element in the inner array
        cout << col << endl;
int count,incr;int var = (count=19,  incr=10, count+1);            //逗号表达式,var的值为最右边的表达式的值,此例为20
int main(int argc, char* argv[]) {}
void f(void){} atexit(f) //注册程序正常终止时要被调用的函数,最多可以注册32个处理函数，这些处理函数的调用顺序与注册顺序相反，即后注册的函数先被调用。
static constexpr int mod=1E9+7;     //const int MOD = 1000000007
max(max(a,b),c);                             //min({1,2,3})
floor();ceil();round()                           //向下取整、向上取整、四舍五入
gcd(int a,int b)                                 //求最大公约数
pow(a,b)   //返回double a**b
int mx=*max_element(dp,dp+26)   //*min_element(vec.begin(),vec.end())
int index = max_element(arr.begin(), arr.begin() + n) - arr.begin();
move(obj);   //将一个对象转换为另一个对象，左值引用转换为右值引用，可以避免不必要的拷贝操作
reverse(s,s+9);     //参数一是翻转的第一项，参数二是翻转后的一项,reverse(s.begin(),s.begin()+9)
iota(ans.begin(), ans.end(), 0);  //将ans赋值为0开始的值
swap(s[i],s[j]);
accumulate(arr.begin(),arr.end(),0);    //求和(string也可以,初始元素为“”s或者string{})  
accumulate(arr.begin(),arr.end(),0,op);  //op是二元函数对象，常为lambda表达式，参1总数，参2arr元素
count(vec.begin(),vec.end(),8);         //count(a,a+n,7)
count_if(vec.begin(),vec.end(),[](int a){return a>10;});
sort(arr,arr+n,greater<int>());//compare默认为less升序,stable_sort(strArray.begin(), strArray.end(), compare); 稳定排序
bool compare(stu a,stu b){     //自定义compare，常用lambda表达式如sort(costs.begin(), costs.end(), [](vector<int> &a, vector<int> &b){return a[0] - a[1] < b[0] - b[1];});   
	if(a.d+a.c!=b.d+b.c) return a.d+a.c>b.d+b.c;
	else if(a.d!=b.d) return a.d>b.d;
	else return a.id<b.id;
}
nth_element(vec.begin(), vec.begin()+2, vec.end());
nth_element (RandomAccessIterator first,            //默认升序，找到序列中第n小的元素K，并将 K 移动到序列中第 n 的位置处
                  RandomAccessIterator nth,         //而且所有位于 K 之前的元素都比 K 小，所有位于 K 之后的元素都比 K 大。
                  RandomAccessIterator last,        //适用于 array、vector、deque 这 3 个容器以及普通数组
                  Compare comp);                    //自定义compare
auto it=upper_bound(times.begin(), times.end(), t); //二分查找,序列中大於t的最小值的位置(地址)，减去times.begin()即为序号
int pos3=lower_bound(num,num+6,7,greater<int>())-num;  //返回数组中第一个小于或等于被查数的值，重载为greater降序序列
int k = upper_bound(jobs.begin(), jobs.begin() + i - 1, jobs[i - 1][0], [&](int st, const vector<int> &job) -> bool {
    return st < job[1];
}) - jobs.begin();
[int]b=n/100%10;s=n/10%10;g=n%10;                      //百位，十位，个位
bool isPrime(int n){                              //判断素数
 bool yes=true;
 for(int i=2;i<=sqrt(n);i++){
  if(n%i==0){yes=false;break;}
 }
 return yes;
}
int year{2008};year % 400 == 0 || (year % 4 == 0 && year % 100 != 0 )//判断闰年
ListNode* dummy = new ListNode(-1);TreeNode* root = new TreeNode(0);
/*静态成员函数指针=普通函数指针!=成员函数指针*/
lambda表达式 [capture list](params list) |mutable| |exception| |-> return type| { function body };
/*capture list：捕获外部变量列表  [=]表示以值捕获的方式捕获外部变量，[&]表示以引用捕获的方式捕获外部变量 混合捕获[&, c]、[=, &os]
params list：形参列表
mutable指示符：用来说用是否可以修改捕获的变量
exception：异常设定
return type：返回类型
function body：函数体*/
sort(words.begin(),words.end(),[](const string &a,const string &b){return a.size()==b.size()?a>b:a.size()<b.size();});
function<void(TreeNode*,int)> dfs = [&](TreeNode* node,int cur) {... dfs(node->left,cur+1);};   //lambda递归型
function<bool(int,int)> dfs=[&](int s,int p)->bool{...};
all_of(iter1,iter2,func)    //迭代范围内的每个元素满足指定属性返回true,常与lambda表达式连用
transform(first1, last1, result, op)//需返回值并将每个操作返回的值存储在以result开头的范围内，op可以是函数指针或函数对象或lambda表达式
transform(first1, last1, first2, result, op) //使用[first1, last1)范围内的每个元素作为第一个参数调用op,并以first2开头的范围内的每个元素作为第二个参数调用op
for_each(first1,last1,op)                    //速度快但要求一个序列，将op应用于[first1, last1)范围内的每个元素，无需返回值
find_if(words.begin(), words.end(),op);      //对序列中的每个元素调用op，并返回第一个返回true的迭代器。如果不存在，则返回尾迭代器。
```

## 数组
```c++
int dp[26]={0};int len=sizeof(dp)/sizeof(int);
```

## string
```c++
string s(); string s("hello"); string s(4,'k'); string s1(s,1,3)    //s从1开始长度为3的子串 不支持一个字符型参数的构造函数
s="hello"; s='k'; s1.assign(s,1,3)
s.size(); s.length()
for(char& c:str);int num=c-'a';char c=num+'0';
s.append(3,'a'); s1.append(s,1,3)   //追加字符(需要添加个数参数)或字符串    s.insert(2,3,'k') //在下标2处添加字符串"kkk"
s.push_back(); s.pop_back(); //添加|删除字符
string num = to_string(sum);//数值转字符串 
str.find(string target,int m,int n);        //从str的m位置开始查找目标str的前n个字符，返回第一个首字母位置 str.find("jxq")!=string::npos;str.rfind()
string str2[10] = {"ling","yi","er","san","si","wu","liu","qi","ba","jiu"};string a(5,'8');string *str = {"hello", "world"};
char str[14] = {"0123456789JQK"};char str[10]={'I','','a','m','','h','a','p','p','y'};char *str[] = {"Hello", "C++", "World"};char *str="IloveChina";
s1=s.substr(i,b);//复制子字符串，从指定位置i开始，指定长度b
s1.swap(s)
char * strtok (char * str, const char * delimiters);//将字符串分割成一个个片段,str指向欲分割的字符串(char []型不可是string)，delimiters为分割符(支持多个)
sch[1]=tolower(sch[1]);//转小写
if(s2[i]>='a'&&s2[i]<='z'){
	s2[i]+='A'-'a';      //小写转大写
}
'''字符c大小写转换可以使用 `c ^ 32` '''
transform(str1.begin(), str1.end(), str1.begin(), ::toupper);
vector<string> split(const string &str,char trim){
    int n=str.size();
    vector<string> res;
    int pos=0;
    while(pos<n){
        while(pos<n&&str[pos]==trim){
            pos++;
        }
        if(pos<n){
            int curr=pos;
            while(pos<n&&str[pos]!=trim){
                pos++;
            }
            res.emplace_back(str.substr(curr,pos-curr));
        }
    }
    return res;
}
str1.comapre(pos1,cnt1,str2,pos2,cnt2)   //两个串值相同，则函数返回 0；若字符串 S1 按字典顺序要先于 S2，则返回负值；反之，则返回正值
```
string转int `stoi(s)`也可以是`atoi(s.c_str())`，转成double、float `stod() atof()`     <br>
`isalpha(s3[i])`判断是否为英文字母、`isdigit()`数字 <br>
 stringstream 主要是用在將一個字串分割，先用 clear() 以及 str() 將指定字串設定成一开始的內容，再用 >> 把个別的资料输出 <br>
 string_view   <br>

## stl
list双向链表   deque双端队列 priority_queue优先队列                           <br>
```c++
pair<string,string> p(file,row);
priority_queue<int> pq1; pq1.emplace(1); pq1.push(2);   //大顶堆
priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq2;	pq2.push({0, 1});  //小顶堆
unordered_map<strinig,list<pair<unordered_set<string>,int>>> nodes;
//手写unordered_map
static constexpr auto tri_hash = [fn = hash<int>()](const tuple<int, int, int>& o) -> size_t {
        auto&& [x, y, z] = o;
        return (fn(x) << 24) ^ (fn(y) << 8) ^ fn(z);
    };
unordered_map<tuple<int, int, int>, pair<TreeNode*, int>, decltype(tri_hash)> seen{0, tri_hash};
unordered_map<char,vector<int>> hash;for (auto &&[_, arr]: hash)
unordered_map<string,vector<int>> hash; for(auto &[name,list]:hash)
unordered_set<int> un_set;for(int next:un_set); {un_set.begin(),un_set.end()}//转为vector
set<int> qwe;qwe.insert(2);qwe.insert(1);qwe.erase(qwe.begin());     //插入字符后有序，删除的是1
qwe.insert(s.begin(),s.end());
map<string,int> jxq; jxq.insert(make_pair("2",1)); jxq.erase("3")'删除成功返回1，不成功返回0'
vector<int> vec(n,0);vec={0};vec.push_back({i,j})<=>vec.emplace_back(initializer_list<int>{i,j});vec.erase(vec.begin()【,vec.begin()+n】);vec.emplace(vec.begin(),0); 
vector<vector<int>> vec2(m,vector<int>(n));vec2={{arr[i-1],arr[i]}};
//自定义优先队列compare
struct Status {
    int val;
    ListNode *ptr;
    bool operator < (const Status &rhs) const {
        return val > rhs.val;                          //小根堆 priority_queue <Status> q;

    }
};
struct cmp {
    bool operator()(ListNode* a, ListNode* b){
        return a->val>b->val;                          //小根堆 
    }
};
priority_queue<Ratio,vector<Ratio>,cmp> pq;
```

## 输入输出
设置输出宽度`cout.width(12)`，保留3位有效数字`cout<<setprecision(3)<<a`         <br>
`cout<<setiosflags(ios::right)`   设置右对齐  `cout<<resetiosflags(ios::left)`  清除状态左对齐   <br>
`while(cin.get(c))`遇到正常字符进入while循环，遇到Ctrl z/d退出while            <br>
`while (getline(cin,str))`读入多行字符串                            <br>
`cin.getline(name,20)`读取一行字符串，丢弃换行符,输入字符串可以有空格，读到指定数目字符或遇到换行符停止,字符数组`char name[20]`   <br>
接收含有空格的字符串，采用cin.get(字符数组名，接收字符数目)`cin.get(name,20)`,不再 读取并丢弃换行符，而是将其留在输入队列中，空参数`cin.get()`读取读取一个字符，包括换行符      <br>
printf输出string类型必须使用`.c_str()`   <br>
```c++
getchar();//吃掉回车
printf("%.2f ",A4);//保留两位有效数字
printf("%04d - %04d = %04d\n", max, min,n);//4位整数输出;printf中双引号内除了输出控制符和转义字符\n外，所有其余的普通字符全部都原样输出
printf("%.1f%% %.1f%%\n", 1.0*count1/N*100, 1.0*count2/N*100);//输出百分数两个百分号
sscanf(log.c_str(), "%d:%[^:]:%d", &idx, type, &timestamp);//{"0:start:0","0:end:2"}
```

## 类和结构
```c++
TreeNode* node=new TreeNode(val);
struct student
{
    string name;
    int score;
    student(int _name,string _score):name(_name),score(_score){}               //初始化列表
};
class Arr{
public:
    Arr(int n){
        data =new int[n];
    }
    ~Arr(){
        delete []data;
    }
private:
    int *data;                  //动态数组
};
```

