#include <bits/stdc++.h>
using namespace std;

int main() {
  int n,a;
  scanf("%d",&n);
  vector<int> paths[n];
  int ans[n];
  int cnt[n];
  memset(ans,0,sizeof ans);
  memset(cnt,0,sizeof cnt);
  for (int i=1;i<n;i++){
    scanf("%d",&a);
    paths[a-1].push_back(i);
  }
  queue<int> q;
  q.push(0);
  while (!q.empty()){
    a = q.front();
    q.pop();
    for (int i:paths[a]){
      if (!ans[i]){
        ans[i] = ans[a]+1;
        cnt[ans[i]]++;
        q.push(i);
      }
    }
  }
  int res = 0;
  for (int i=0;i<n;i++){
    if (cnt[i]%2) res++;
  }
  printf("%d\n",res+1);
}
