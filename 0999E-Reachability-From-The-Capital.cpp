#include <bits/stdc++.h>
using namespace std;

int main() {
  int n,m,s,a,b;
  scanf("%d %d %d",&n,&m,&s);
  vector<int> paths[n];
  int paths2[n];
  int checked[n];
  pair<int,int> vals[n];
  int temp[n];
  for (int i=0;i<n;i++){
    vals[i] = {0,i};
    checked[i] = 0;
    paths2[i] = 0;
  }
  for (int i=0;i<m;i++){
    scanf("%d %d",&a,&b);
    a--;
    b--;
    paths[a].push_back(b);
    paths2[b]++;
  }
  queue<int> q;
  q.push(s-1);
  checked[s-1] = 1;
  while (!q.empty()){
    a = q.front();
    q.pop();
    for (int i:paths[a]){
      if (!checked[i]){
        checked[i] = 1;
        q.push(i);
      }
    }
  }
  int ans = 0;
  for (int i=0;i<n;i++){
    if (!checked[i]&&!paths2[i]){
      q.push(i);
      checked[i] = 1;
      ans++;
      while (!q.empty()){
        a = q.front();
        q.pop();
        for (int j:paths[a]){
          if (!checked[j]){
            checked[j] = 1;
            q.push(j);
          }
        }
      }
    }
  }
  for (int i=0;i<n;i++){
    if (!checked[i]){
      for (int j=0;j<n;j++){
        temp[j] = 0;
      }
      q.push(i);
      temp[i] = 1;
      int res = 1;
      while (!q.empty()){
        a = q.front();
        q.pop();
        for (int j:paths[a]){
          if (!temp[j]){
            temp[j] = 1;
            res++;
            q.push(j);
          }
        }
      }
      vals[i].first = res;
    }
  }
  sort(vals,vals+n);
  int cnt = 0;
  for (int i=0;i<n;i++){
    cnt += checked[i];
  }
  for (int i=n-1;n>=0;i--){
    if (cnt==n) break;
    if (checked[vals[i].second]) continue;
    q.push(vals[i].second);
    checked[vals[i].second] = 1;
    ans++;
    cnt++;
    while (!q.empty()){
      a = q.front();
      q.pop();
      for (int j:paths[a]){
        if (!checked[j]){
          checked[j] = 1;
          cnt++;
          q.push(j);
        }
      }
    }
  }
  printf("%d\n",ans);
}
