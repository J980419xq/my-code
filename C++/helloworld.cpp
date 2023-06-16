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
#include <sstream>
#define pair1 pair<int, int>
#define pair2 pair<int, pair1>
using namespace std;

class unionSet{
private:
    int *fa,*rank;
public:
	unionSet(int n){
		fa=new int[n+1];rank=new int[n+1];
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
void quickSort(vector<int>& arr,int l, int r,int k){                         //快排
	if(l>=r)return;
	int i=l,j=r,pivot=arr[l];
	while(i<j){
		while(i<j&&arr[j]>=pivot){
			j--;
		}
		arr[i]=arr[j];
		while(i<j&&arr[i]<=pivot){
			i++;
		}
		arr[j]=arr[i];
	}
	arr[i]=pivot;
	if(i>k)quickSort(arr,l,i-1,k);
	if(i<k)quickSort(arr,i+1,r,k);
	return ;
}


template <typename T, typename F>
T use_f(T v, F f)
{
	return f(v);
}

bool compare(vector<int> &a, vector<int> &b)
{
	return a[0] - a[1] < b[0] - b[1];;
}
bool check_mask(string mask){
    istringstream iss(mask);
    string seg;
    unsigned b=0;
    while(getline(iss,seg,'.'))b=(b<<8)+stoi(seg);
    if(b==0)return false;
    b=~b+1;
    if(b==1)return false;
    if((b&(b-1))!=0)return false;
    return true;
}
bool check_ip(string ip){
    int j=0;
    istringstream iss(ip);
    string seg;
    while(getline(iss,seg,'.')){
        if(seg.empty()||stoi(seg)>255||stoi(seg)<0){
            return false;
        }
        j++;
    }
    return j==4;
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
