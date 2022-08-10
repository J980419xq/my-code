#！/usr/bin/env python
from cmath import nan
import random
import pandas as pd
import matplotlib.pyplot as plt
font = {'family' : 'SimHei',
        'weight' : 'bold',
        'size'   : '10'}
plt.rc('font', **font)
print(random.random())
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 23, 58],
        "Sex": ["male", "male", "female"],
    }
)
ages = pd.Series([22, 23, 24], name="Age")#df["Age"]
test=pd.read_excel("D:/MyCode/Python/19ea4a20ab617fd3586004646990f44a_ad6e2b03b208ef1ed85a05605a08ce3a_8.xlsx",sheet_name="car_selling_target")   #路径用/
#test[test["company"].isin(["一汽大众","广汽本田"])])<=>print(test[(test["company"]=="一汽大众")|(test["company"]=="广汽本田")]
#test.loc[test["total_target"]>75,["company","total_target"]],test.iloc[20:30,0:2],test.iloc[20:30,0]="宝马"
#df,df.head(2),df.tail(2),df.describe(),df.info(),df.shape,df.dtypes,
#df["Name"][2],df[["Name","Age"]],df[df["Age"]>23],df["Age"].max【mean,median】(),df[df["Age"].notna()],sum(ages),df[0:5]
fig, ax1 = plt.subplots(figsize=(8,6))
labels=list(set(test["company"]))
for label in labels:
    ax1.plot(["2015","2016","2017","2018","2019"],test.loc[test["company"]==label,"total_target"],label=label)
ax1.legend()
test.plot.area(figsize=(12,4),subplots=True)
test1=test.iloc[5:10,2:3]
fig, ax2 = plt.subplots(figsize=(8,6))
test1.plot.area(ax=ax2)
ax2.set_title("demo")
test1.plot.box()
#plt.show()
for i in range(len(test["company"])):
    if i==0 or test["company"][i-1]!=test["company"][i] or pd.isna(test["total_target"][i-1]):
        test.loc[i,'rate']=1
    elif not pd.isna(test["total_target"][i]):
        test.loc[i,'rate']=(test["total_target"][i]-test["total_target"][i-1])/test["total_target"][i-1]
test[["company","total_target"]].groupby("company").mean()
test["company"].value_counts()     #<=>test.groupby("company")["company"].count(),count不包含NaN,而size等价为行数
test.groupby("company")["total_target"].mean()                #注意与上面的区别,groupby可将包含多个列的列表作为参数
test.agg({
    "total_target": ["min", "max", "median", "skew"],
})
test2=test.rename(                 #返回新对象,原对象不做修改
    columns={                      #columns=str.upper()
        "total_target":"target",
    }
)
test2.index+=1
#test.to_excel("D:/MyCode/Python/test.xlsx", sheet_name="passengers", index=False)
n=1024
n=list(str(n))                     #['1', '0', '2', '4']
n=list(map(int,n))                 #[1, 0, 2, 4]
n=n[-1::-1]                        #[4, 2, 0, 1]
arr=[3,2,4,5,3]
arr2=sorted(set(arr))              #arr不变,arr2[2, 3, 4, 5]
arr.sort(reverse=True)             #arr变,reverse=True降序,默认升序
parent=list(range(4))              #[0,1,2,3]
map={"jxq":1,"yyh":2}
lst = list( map.items() )          #[('jxq', 1), ('yyh', 2)]