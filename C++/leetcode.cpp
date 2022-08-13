#include <vector>
#include <queue>
#include <algorithm>
#include <numeric>
#include <unordered_set>
#include <iostream>
using namespace std;
class Solution{
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int n=nums.size();
        if(n==(k*3)){
            return {0,k,2*k};
        }
        vector<int> ans;
        int mmax=0;
        for(int i=0;i+3*k<=n;i++){
            int temp=accumulate(nums.begin()+i,nums.begin()+i+k,0);
            for(int j=i+k;j+2*k<=n;j++){
                int temp1=temp+accumulate(nums.begin()+j,nums.begin()+j+k,0);
                for(int l=j+k;l+k<=n;l++){
                    int cur=temp1+accumulate(nums.begin()+l,nums.begin()+l+k,0);
                    if(cur>mmax){
                        ans.clear();
                        ans.emplace_back(i);
                        ans.emplace_back(j);
                        ans.emplace_back(l);
                        mmax=cur;
                    }
                }
            }
        }
        
        return ans;
    }
};
int main(){
    Solution solution=Solution();
    vector<int> nums={1,2,1,2,6,7,5,1};
    vector<int> ans;
    ans=solution.maxSumOfThreeSubarrays(nums,2);
    for(int& num:ans){
        cout<<num<<" ";
    }
    return 0;
}