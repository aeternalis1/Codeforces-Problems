#include <bits/stdc++.h>
using namespace std;

int main() {
  int n,d,k;
  scanf("%d %d %d",&n,&d,&k);
  if (d>=n||n>2&&k==1){
    printf("NO\n");
    return 0;
  }
  int edges = n-1;
  int cur;
  vector<int> paths[n];
  vector<int> ans[n];
  int cnt[n];
  memset(cnt,0,sizeof cnt);
  int ind = 1;
  queue<int> q;
  q.push(d/2);
  if (d%2) q.push(d/2+1);
  int l = d/2-1;
  int r = d/2+1;
  if (d%2) r++;
  for (int i=0;i<d;i++){
    paths[i].push_back(i+1);
    paths[i+1].push_back(i);
    ans[i].push_back(i+1);
    cnt[i]++;
    cnt[i+1]++;
    edges--;
    ind++;
  }
  while (!q.empty()){
    int len = (int)q.size();
    for (int _=0;_<len;_++){
      cur = q.front();
      q.pop();
      int need = ind+k-cnt[cur];
      for (int i=ind;i<need;i++){
        if (!edges) break;
        edges--;
        paths[i].push_back(cur);
        paths[cur].push_back(i);
        ans[cur].push_back(i);
        cnt[i]++;
        q.push(i);
        ind++;
      }
    }
    if (l>=0){
      q.push(l);
      l--;
    }
    if (r<=d){
      q.push(r);
      r++;
    }
  }
  q.push(n-1);
  int checked[n];
  memset(checked,0,sizeof checked);
  checked[n-1] = 1;
  while (!q.empty()){
    cur = q.front();
    q.pop();
    for (int i:paths[cur]){
      if (!checked[i]){
        checked[i] = checked[cur]+1;
        q.push(i);
      }
    }
  }
  int res = 0;
  ind = 0;
  for (int i=0;i<n;i++){
    if (checked[i]>res){
      res = checked[i];
      ind = i;
    }
  }
  q.push(ind);
  memset(checked,0,sizeof checked);
  checked[ind] = 1;
  while (!q.empty()){
    cur = q.front();
    q.pop();
    for (int i:paths[cur]){
      if (!checked[i]){
        checked[i] = checked[cur]+1;
        q.push(i);
      }
    }
  }
  res = 0;
  for (int i=0;i<n;i++){
    if (checked[i]>res){
      res = checked[i];
    }
  }
  if (res-1==d){
    printf("YES\n");
    for (int i=0;i<n;i++){
      for (int j:ans[i]){
        printf("%d %d\n",i+1,j+1);
      }
    }
  }else{
    printf("NO\n");
  }
}
