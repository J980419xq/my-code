#include <queue>
#include <cstring>
#include <iostream>
#include <unordered_set>
#include <set>
#include <unordered_map>
#include <map>
#include <vector>
#include <algorithm>
#include <functional>
#define pair1 pair<int, int>
#define pair2 pair<int, pair1>
using namespace std;

template <typename T, typename F>
T use_f(T v, F f)
{
	return f(v);
}

int selection(string a, string b)
{
	int sum = 0;
	for (char c : a)
	{
		for (char s : b)
		{
			if (c == s)
			{
				sum++;
			}
		}
	}
	return sum;
}
bool compare(vector<int> &a, vector<int> &b)
{
	return a[0] - a[1] < b[0] - b[1];;
}

int main()
{
	function<int(int)> func = [&](int n) {
		return n == 1 ? 1 : n + func(n - 1);
	};
	int n=7;
	set<int> qwe;
	qwe.insert(2);
	qwe.insert(1);
	qwe.erase(qwe.begin());     //插入字符后有序，删除的是1
	priority_queue<int, vector<int>, less<int>> q;    //默认，大顶堆
	priority_queue<pair1, vector<pair1>, greater<pair1>> pq1;
	priority_queue<pair2, vector<pair2>, greater<pair2>> pq2;
	q.emplace(1); //q.push(2);
	pq1.push({0, 1});
	pq2.push({{0}, {1, 2}});
	
	map<string,int> jxq;
	jxq.insert(make_pair("2",1));
	jxq.insert(make_pair("1",2));
	jxq.insert(make_pair("3",3));
	jxq.insert(make_pair("3",4));
	/*for(map<string,int>::iterator iter=jxq.begin();iter!=jxq.end();++iter){
		cout<<iter->first<<" "<<iter->second<<endl;
	}                         插入有序*/ 
	//cout<<jxq.erase("3");                 //删除成功返回1，不成功返回0
	/*int n=0;
	n|=1<<('b'-'a');
	n|=1<<('c'-'a');
	cout<<(1<<('c'-'a'))<<endl;*/
	int b[5] = {1, 3, 6, 7, 2};
	unordered_set<int> unset(b,b+5);
	/*for(int x:unset){
		cout<<x<<" ";
	}*/
	cout<<endl;
	vector<vector<int>> d;
	d.push_back({1,2});
	d.push_back({1,3});
	d.push_back({1,1});
	auto res = lower_bound(b, b + 5, 3) - b;
	unordered_map<char,int> htable;
	vector<int> score(b, b + 5);
	unordered_map<int, int> mapp;    //默认值为0
	n = score.size();
	for (int i = 0; i < n; ++i)
	{
		mapp[score[i]] = i;
	}
	
	vector<int> c(3, 5);
	vector<string> ans(n, "0");
	vector<vector<int>> f(3, vector<int>(3, 2));
	string str[] = {"hello", "wrd", "this", "find", "gank", "pink", "that", "when", "how", "cpp"};
	vector<string> strArray(str, str + 10);
	//stable_sort(strArray.begin(), strArray.end(), compare); 稳定排序
	sort(d.begin(),d.end(),compare);

	/*int m = [](int x) { return [](int y) { return y * 2; }(x)+6; }(5);   //lambda表达式
    std::cout << "m:" << m << std::endl;            //输出m:16
	std::cout << "n:" << [](int x, int y) { return x + y; }(5, 4) << std::endl;            //输出n:9*/
    string s="313";
	
	string word;
	for(auto &c:s){
		word.append(4,'.');
	}
	return 0;
}
