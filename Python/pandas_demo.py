#！/usr/bin/env python
from cmath import nan
from operator import index
import random
import pandas as pd
import matplotlib.pyplot as plt
###pandas和matplotlib处理表格数据(excel)pandas使用apply()处理python代码
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
            "Yuehe, Miss. Yu"
        ],
        "Age": [22, 23, 58,23],
        "Sex": ["male", "male", "female","female"],
    }
)
ages = pd.Series([22, 23, 24], name="Age")#df["Age"]
test=pd.read_excel("D:/MyCode/Python/19ea4a20ab617fd3586004646990f44a_ad6e2b03b208ef1ed85a05605a08ce3a_8.xlsx",sheet_name="car_selling_target")   #路径用/
#test[test["company"].isin(["一汽大众","广汽本田"])])<=>print(test[(test["company"]=="一汽大众")|(test["company"]=="广汽本田")]
#test.loc[test["total_target"]>75,["company","total_target"]],test.iloc[20:30,0:2],test.iloc[20:30,0]="宝马",df.loc[df["Name"].str.len().idxmax(),"Name"]
#df,df.head(2),df.tail(2),df.describe(),df.info(),df.shape,df.dtypes,
#df["Name"][2],df[["Name","Age"]],df[df["Age"]>23],df["Age"].max【mean,median】(),df[df["Age"].notna()],sum(ages),df[0:5]
#df["Name"].str.lower(),df["Name"].str.split(",").str.get(0),df["Name"].str.contains("Yuehe"),df["Sex"].replace({"male": "M", "female": "F"})
fig, ax1 = plt.subplots(figsize=(8,6))
labels=test.company.unique()
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
test.groupby(["year","company"])["total_target"].mean()              #注意与上面的区别,groupby可将包含多个列的列表作为参数
test.sort_values(by=["company","total_target"], na_position='first',ascending=False)
test.sort_index().groupby("company")[["company","total_target"]].head(2)
test.agg({
    "total_target": ["min", "max", "median", "skew"],
})
test2=test.rename(                 #返回新对象,原对象不做修改
    columns={                      #columns=str.upper()
        "total_target":"target",
    }
)
test2.index+=1
test.pivot_table(values=['total_target','total_amount'],index="company",aggfunc="mean",margins=True,)
test.set_index(["year"], inplace=True)
test2=test.pivot(columns='company',values='total_target').reset_index()
test2.melt(id_vars="year",
    value_vars=["一汽丰田","一汽大众","上汽乘用车","东风日产","东风本田","吉利汽车","广汽丰田","广汽乘用车","广汽本田","长城汽车"],
    value_name='total_target',
    var_name="company",)
test2=test[test["company"]=="一汽大众"]
test3=test[test["company"]=="一汽丰田"]
test4=pd.concat([test2,test3],keys=["一汽大众","一汽丰田"],axis=0)         #"0" row , "1" column
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                   'key': ['K0', 'K1', 'K0', 'K1']})
right = pd.DataFrame({'C': ['C0', 'C1'],
                      'D': ['D0', 'D1']},
                    index=['K0', 'K1'])
pd.merge(left, right, left_on='key', right_index=True, how='left', sort=False)
#test.to_excel("D:/MyCode/Python/test.xlsx", sheet_name="passengers", index=False)
