#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long
#define MAXN 200001

int dist;
int arr[MAXN];
vector<int> order;
int lim[MAXN];
vector<int> paths[MAXN];

void dfs(int cur, int par){
  arr[cur] = dist;
  order.push_back(cur);
  dist++;
  for (int i:paths[cur]){
    if (i==par) continue;
    dfs(i,cur);
  }
  lim[cur] = dist;
}

int main(){
  int n,q,a,b,cur;
  scanf("%d %d",&n,&q);
  for (int i=0;i<n-1;i++){
    scanf("%d",&a);
    paths[a-1].push_back(i+1);
    paths[i+1].push_back(a-1);
  }
  for (int i=0;i<n;i++){
    sort(paths[i].begin(),paths[i].end());
  }
  dfs(0,-1);
  for (int i=0;i<q;i++){
    scanf("%d %d",&a,&b);
    a--;
    b--;
    if (arr[a]+b>=n){
      printf("-1\n");
      continue;
    }
    cur = order[arr[a]+b];
    if (arr[cur]>=lim[a]) printf("-1\n");
    else printf("%d\n",cur+1);
  }
}
