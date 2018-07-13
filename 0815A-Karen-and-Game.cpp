#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
  int n,m,cur;
  scanf("%d %d",&n,&m);
  int grid[n][m];
  int temp[n][m];
  int s = 10000;
  for (int i=0;i<n;i++){
    for (int j=0;j<m;j++){
      scanf("%d",&grid[i][j]);
      if (!i) s = min(s,grid[i][j]);
    }
  }
  vector<pair<int,int>> end;
  vector<pair<int,int>> coms;
  int ans = 9999999;
  for (int i=0;i<=s;i++){
    coms.clear();
    bool val = 1;
    for (int j=0;j<n;j++){
      for (int k=0;k<m;k++){
        temp[j][k] = grid[j][k];
        if (!j) temp[j][k]-=i;
      }
    }
    for (int j=0;j<i;j++){
      coms.push_back({0,0});
    }
    for (int j=0;j<m;j++){
      if (temp[0][j]){
        cur = temp[0][j];
        for (int k=0;k<n;k++){
          temp[k][j] -= cur;
          if (temp[k][j]<0) val = 0;
        }
        for (int k=0;k<cur;k++){
          coms.push_back({1,j});
        }
      }
    }
    if (!val) continue;
    for (int j=0;j<n;j++){
      for (int k=1;k<m;k++){
        if (temp[j][k]!=temp[j][0]){
          val = 0;
        }
      }
      if (val){
        for (int k=0;k<temp[j][0];k++){
          coms.push_back({0,j});
        }
      }
    }
    if (val){
      if (coms.size()<ans){
        ans = coms.size();
        end = coms;
      }
    }
  }
  if (ans != 9999999){
    printf("%d\n",ans);
    for (pair<int,int> i:end){
      if (i.first) printf("col %d\n",i.second+1);
      else printf("row %d\n",i.second+1);
    }
  }else{
    printf("-1\n");
  }
}
