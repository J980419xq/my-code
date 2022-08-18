import re
'''正则表达式 
`\w` `\d` `\s` `\b`分别表示匹配一个 字母数字下划线 数字 空白字符 单词边界,转换成大写后取反,如\D匹配一个非数字 `·`匹配一个任意字符(`\n`不能匹配)
`?`匹配前面的re表达式0或1次,非贪婪方式 `+`匹配>=1次 `*`匹配>=0次 `{n}`精确匹配n次 `{n,}`匹配>=n次 `{m,n}`匹配m到n次(贪婪) `{m,n}?`尽量匹配少的
`[]`匹配[]内的一个字符([a-zA-Z0-9]匹配数字字母中的任意一个),需要匹配特殊字符时加`\`([\-]匹配-),开头加上`^`意为取反([^0-9a-z]匹配非数字或小写字母)
[]外`^`匹配字符串开头 `$`匹配字符串结尾 `|`或者关系((a|b)匹配a或b)
`()`提取想要的匹配内容 group(0)永远是与整个正则表达式相匹配的字符串,group(1)、group(2)...表示第1、2、...个子串
	m=re.match(r'(1(a|b))a','1baa')
	m.group(【0】)=='1ba' m.group(1)=='1b' m.groups()==('1b', 'b') m.group(1,2)=='1b' 几个括号就几个字串
'''

re.match(r'(1(a|b))a','1baa')   #从起始位置起匹配,返回一个匹配的对象,否则返回None re.match(pattern,string【,flags=0】)
re.search('com', 'www.runoob.com')   #扫描整个字符串并返回第一个成功的匹配 re.search(pattern,string【,flags=0】)
re.findall(r'(\w+)=(\d+)','set width=20 and height=10')   #在字符串中找到正则表达式所匹配的所有子串,并返回一个列表,如果有多个匹配模式,则返回元组列表,如果没有找到匹配的,则返回空列表
re.finditer(r'(\w+)=(\d+)','set width=20 and height=10')  #类似findall()不过返回的是一个元素为match对象的迭代器 与match、search、findall调用方式一样
str1='2004-959-559#abc'       
str1=re.sub(r'#.*$',"",str1)   #替换字符串的匹配项,返回新字符串 re.sub(pattern,repl,string【,count=0,flags=0】) count:替换的最大次数,默认为0替换所有的匹配
def double(matched):           #repl:替换的字符串,也可为一个函数对匹配的字符进行操作
    value=int(matched.group('value'))
    return str(value*2)
s='A23G4HFD567'
re.sub('(?P<value>\d+)',double,s)   #A46G8HFD1134 r'(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})' groupdict() 可以通过命名引用
re.split('\W+', ' runoob, runoob, runoob.')   #切割字符串re.split(pattern,string【,maxsplit=0,flags=0】) 返回列表 
re.split('(\W+)', ' runoob, runoob, runoob.')   #使用括号捕获分组,默认保留分割符 不想保留分隔符,以(?:...)的形式指定 re.split(r'(?:\W+)',' runoob, runoob, runoob.')
re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')   #预编译,生成一个正则表达式(Pattern)对象 re.compile(pattern【,flags】)
re_telephone.match('010-12345').groups()   #('010','12345') pattern.match(string【,lo【,hi】】)其余方法类似

