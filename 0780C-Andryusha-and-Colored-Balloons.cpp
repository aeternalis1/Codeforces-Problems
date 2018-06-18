#include <bits/stdc++.h>
using namespace std;

#define MAXN 200001

int cols[MAXN];
vector<int> paths[MAXN];

void dfs(int cur, int par){
  int cnt = 1;
  for (int i:paths[cur]){
    if (i==par) continue;
    while (cnt==cols[cur]||cnt==cols[par]) cnt++;
    cols[i] = cnt++;
    dfs(i,cur);
  }
}

int main(){
  int n,a,b;
  scanf("%d",&n);
  for (int i=0;i<n-1;i++){
    scanf("%d %d",&a,&b);
    a--;
    b--;
    paths[a].push_back(b);
    paths[b].push_back(a);
  }
  memset(cols,0,sizeof cols);
  cols[0] = 1;
  cols[n] = -1;
  dfs(0,n);
  int ans = 0;
  for (int i=0;i<n;i++){
    ans = max(ans,cols[i]);
  }
  printf("%d\n",ans);
  for (int i=0;i<n;i++) printf("%d ",cols[i]);
}
