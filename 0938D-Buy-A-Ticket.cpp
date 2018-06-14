#include <bits/stdc++.h>
using namespace std;

int main(){
  long long n,m,a,b,c,cur;
  scanf("%lld %lld",&n,&m);
  vector<pair<int,unsigned long long>> edges[n+1];
  unsigned long long ans[n+1];
  unsigned long long cost[n+1];
  bool checked[n+1];
  vector<pair<unsigned long long,int>> tbd;
  for (int i=0;i<m;i++){
    scanf("%lld %lld %lld",&a,&b,&c);
    edges[a].push_back({b,c*2});
    edges[b].push_back({a,c*2});
  }
  for (int i=1;i<=n;i++){
    scanf("%llu",&cost[i]);
    ans[i] = cost[i];
    tbd.push_back({cost[i],i});
  }
  sort(tbd.begin(),tbd.end());
  queue<int> q;
  for (pair<unsigned long long,int> i:tbd){
    q.push(i.second);
    checked[i.second] = true;
  }
  while (!q.empty()){
    cur = q.front();
    q.pop();
    checked[cur] = false;
    for (pair<int,unsigned long long> i:edges[cur]){
      if (ans[i.first]>ans[cur]+i.second){
        ans[i.first] = ans[cur]+i.second;
        if (!checked[i.first]){
          q.push(i.first);
        }
      }
    }
  }
  for (int i=1;i<=n;i++){
    printf("%llu ",ans[i]);
  }
}
