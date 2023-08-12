#include <vector>
#include <queue>
#include <algorithm>
#include <numeric>
#include <unordered_set>
#include <iostream>
#include <functional>
using namespace std;
class Solution{
public:
    int shortestBridge(vector<vector<int>>& grid) {
        const int stations[4][2]={{0,-1},{0,1},{-1,0},{1,0}};
        bool flag=true;
        int n=grid.size();
        function<void(int,int,int)> dfs = [&](int i,int j,int k) {
            grid[i][j]=k;
            for(auto& station:stations){
                int x=i+station[0],y=j+station[1];
                if(x>=0&&x<n&&y>=0&&y<n&&grid[x][y]==1){
                    dfs(x,y,k);
                }
            }
            
        };
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(flag&&grid[i][j]==1){
                    flag=false;
                    dfs(i,j,2);
                }
                else if(grid[i][j]==1){
                    dfs(i,j,3);
                }
            }
        }
        int ans=INT_MAX;
        function<void(int,int,int)> f = [&](int i,int j,int k) {
            if(grid[i][j]==3){
                ans=min(ans,k);
                return ;
            }
            for(auto& station:stations){
                int x=i+station[0],y=j+station[1];
                if(x>=0&&x<n&&y>=0&&y<n&&grid[x][y]!=2){
                    f(x,y,k+1);
                }
            }
            
        };
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==2){
                    f(i,j,0);
                }
            }
        }
        return ans;
    }
};
int main(){
    Solution solution=Solution();
    vector<vector<int>> grid({{1, 2}, {2, 3}});
    cout << solution.shortestBridge(grid) << endl;
    return 0;
}