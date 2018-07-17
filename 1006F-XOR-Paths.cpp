#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long
#define MAXN 200001

struct path{
  int y,x;
  ll c;
};

int main(){
  int n,m;
  ll k;
  scanf("%d %d %llu",&n,&m,&k);
  unordered_map<ll,ll> opt[n][m];
  unordered_map<ll,ll> opt2[n][m];
  ll grid[n][m];
  ll ans = 0;
  path cur;
  for (int i=0;i<n;i++){
    for (int j=0;j<m;j++){
      scanf("%llu",&grid[i][j]);
    }
  }
  queue<path> q;
  q.push({0,0,grid[0][0]});
  opt[0][0][grid[0][0]]++;
  while (!q.empty()){
    cur = q.front();
    q.pop();
    if (cur.x+cur.y==(n+m-2)/2){
      continue;
    }
    if (cur.y<n-1){
      opt[cur.y+1][cur.x][cur.c^grid[cur.y+1][cur.x]]++;
      q.push({cur.y+1,cur.x,cur.c^grid[cur.y+1][cur.x]});
    }
    if (cur.x<m-1){
      opt[cur.y][cur.x+1][cur.c^grid[cur.y][cur.x+1]]++;
      q.push({cur.y,cur.x+1,cur.c^grid[cur.y][cur.x+1]});
    }
  }
  q.push({n-1,m-1,k});
  opt2[n-1][m-1][k]++;
  while (!q.empty()){
    cur = q.front();
    q.pop();
    if (cur.x+cur.y==(n+m-2)/2){
      ans += opt[cur.y][cur.x][cur.c]*opt2[cur.y][cur.x][cur.c];
      opt2[cur.y][cur.x][cur.c] = 0;
      continue;
    }
    if (cur.y>0){
      opt2[cur.y-1][cur.x][cur.c^grid[cur.y][cur.x]]++;
      q.push({cur.y-1,cur.x,cur.c^grid[cur.y][cur.x]});
    }
    if (cur.x>0){
      opt2[cur.y][cur.x-1][cur.c^grid[cur.y][cur.x]]++;
      q.push({cur.y,cur.x-1,cur.c^grid[cur.y][cur.x]});
    }
  }
  printf("%llu\n",ans);
}
