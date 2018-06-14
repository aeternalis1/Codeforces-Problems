#include <bits/stdc++.h>
using namespace std;

int main() {
  int N,M,K,S,a,b,c;
  scanf("%d %d %d %d",&N,&M,&K,&S);
  queue<int> q[K];
  vector<int> paths[N];
  int ans[N][K];
  memset(ans,0,sizeof ans);
  for (int i=0;i<N;i++){
    scanf("%d",&a);
    q[a-1].push(i);
    ans[i][a-1] = 1;
  }
  for (int i=0;i<M;i++){
    scanf("%d %d",&a,&b);
    paths[--a].push_back(--b);
    paths[b].push_back(a);
  }
  for (int i=0;i<K;i++){
    while (!q[i].empty()){
      c = q[i].front();
      q[i].pop();
      for (int j:paths[c]){
        if (!ans[j][i]){
          ans[j][i] = ans[c][i]+1;
          q[i].push(j);
        }
      }
    }
  }
  int res;
  for (int i=0;i<N;i++){
    sort(ans[i],ans[i]+K);
    res = 0;
    for (int j=0;j<S;j++){
      res += ans[i][j];
    }
    printf("%d ",res-S);
  }
}
