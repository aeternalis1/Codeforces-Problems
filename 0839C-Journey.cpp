#include <bits/stdc++.h>
using namespace std;

#define MAXN 100001

double ans = 0;
vector<int> paths[MAXN];
int leaves[MAXN];

void dfs(int cur, int par, double prob, int dist){
  if (leaves[cur]) ans += dist*prob;
  for (int i:paths[cur]){
    if (i==par) continue;
    if (!cur) dfs(i,cur,prob/(paths[cur].size()),dist+1);
    else dfs(i,cur,prob/(paths[cur].size()-1),dist+1);
  }
}

int main(){
  int n,a,b;
  scanf("%d",&n);
  for (int i=0;i<n-1;i++){
    scanf("%d %d",&a,&b);
    paths[--a].push_back(--b);
    paths[b].push_back(a);
  }
  for (int i=0;i<n;i++){
    if (paths[i].size()==1) leaves[i] = 1;
  }
  dfs(0,-1,1,0);
  printf("%.9lf\n",ans);
}
