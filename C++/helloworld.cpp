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
#include <cmath>
#define pair1 pair<int, int>
#define pair2 pair<int, pair1>
using namespace std;

class unionSet{
private:
    int *fa,*rank;
public:
	unionSet(int n){
		fa=new int[n];rank=new int[n];
		for (int i = 1; i <= n; ++i)
		{
			fa[i] = i;
			rank[i] = 1;
		}
	}
	~unionSet(){
        delete []fa;
		delete []rank;
    }
	int find(int x)
	{
		return x == fa[x] ? x : (fa[x] = find(fa[x]));
	}
	void merge(int i, int j)
	{
		int x = find(i), y = find(j);
		if (rank[x] <= rank[y])
			fa[x] = y;
		else
			fa[y] = x;
		if (rank[x] == rank[y] && x != y)
			rank[y]++;
	}
};

template <typename T, typename F>
T use_f(T v, F f)
{
	return f(v);
}

bool compare(vector<int> &a, vector<int> &b)
{
	return a[0] - a[1] < b[0] - b[1];;
}

int main()
{
	function<int(int)> func = [&](int n) {
		return n == 1 ? 1 : n + func(n - 1);   //lambda递归
	};
	int l=-1%4;                //负数余数为负数
	int n=7;unionSet uset(n);  //并查集
	vector<string> field={"123","234"};   //cout<<field[1][1]; 
	return 0;
}
