$n^2$
### 常见函数
```c++
max(max(a,b),c)                             //min()
int mx=*max_element(dp,dp+26)   //*min_element(vec.begin(),vec.end())
move(obj);   //将一个对象转换为另一个对象，类似于类型转换
reverse(s,s+9);     //参数一是翻转的第一项，参数二是翻转后的一项,reverse(s.begin(),s.begin()+9)
iota(ans.begin(), ans.end(), 0);  //将ans赋值为0开始的值
```

### 数组
```c++
int dp[26]={0};int len=sizeof(dp)/sizeof(int);
```

### string
```
for(char& c:str);int num=c-'a';
```

### stl
list双向链表   deque双端队列 priority_queue优先队列
```c++
unordered_map<strinig,list<pair<unordered_set<string>,int>>> nodes;
unordered_set<int> un_set;for(int next:un_set);
vector<int> vec(n,0);vec={0};vec.push_back({i,j})<=>vec.emplace_back(initializer_list<int>{i,j});
    vec.insert()
vector<vector<int>> vec2(m,vector<int>(n));vec2={{arr[i-1],arr[i]}};
```

### 位运算
检查一个数是否为 2 的幂: `x > 0 and x & (x - 1) == 0`  <br>
将x最低为的1变为0 `x&(x-1)`                            <br>
取出 x 的二进制表示中最低位那个1 `x & -x `              <br>
检查一个数的二进制表示全为1  `(a & (a + 1)) == 0`       <br>
奇偶判断 `x&1==0`

### 输入输出
设置输出宽度`cout.width(12)`，保留3位小数`cout<<setprecision(3)<<a`         <br>
`while(cin.get(c))`遇到正常字符进入while循环，遇到Ctrl z退出while            <br>
`cin.getline(name,20)`读取一行字符串，丢弃换行符,输入字符串可以有空格，读到指定数目字符或遇到换行符停止,字符数组`char name[20]`   <br>
接收含有空格的字符串，采用cin.get(字符数组名，接收字符数目)`cin.get(name,20)`,不再 读取并丢弃换行符，而是将其留在输入队列中，空参数`cin.get()`读取读取一个字符，包括换行符
```c++
getchar();//吃掉回车
printf("%.2f ",A4);//保留两位有效数字
printf("%04d - %04d = %04d\n", max, min,n);4位整数输出;printf 中双引号内除了输出控制符和转义字符\n外，所有其余的普通字符全部都原样输出
printf("%.1f%% %.1f%%\n", 1.0*count1/N*100, 1.0*count2/N*100);//输出百分数两个百分号
```
printf输出string类型必须使用`.c_str()`