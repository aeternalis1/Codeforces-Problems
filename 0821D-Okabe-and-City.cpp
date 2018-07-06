#include <bits/stdc++.h>
using namespace std;

bitset<10000> adj[10000];

int main() {
  short n,m,k,a,b,ind,c;
  scanf("%hu %hu %hu",&n,&m,&k);
  pair<short,short> pts[k];
  vector<pair<short,short>> xs[m+1];
  vector<pair<short,short>> ys[n+1];
  vector<pair<short,short>> paths[k];
  short ans[k];
  short res = 10001;
  bool checked[k];
  for (int i=0;i<k;i++){
    scanf("%hu %hu",&a,&b);
    ans[i] = 10001;
    checked[i] = 0;
    if (a==1&&b==1){
      ind = i;
    }
    pts[i] = {a,b};
    for (pair<short,short> j:xs[b]){
      if (adj[i][j.second]) continue;
      adj[i][j.second] = adj[j.second][i];
      if (abs(j.first-a)==1){
        paths[i].push_back({j.second,0});
        paths[j.second].push_back({i,0});
      }else{
        paths[i].push_back({j.second,1});
        paths[j.second].push_back({i,1});
      }
    }
    if (b>1){
      for (pair<short,short> j:xs[b-1]){
        if (adj[i][j.second]) continue;
        adj[i][j.second] = adj[j.second][i];
        paths[i].push_back({j.second,1});
        paths[j.second].push_back({i,1});
      }
    }
    if (b<m){
      for (pair<short,short> j:xs[b+1]){
        if (adj[i][j.second]) continue;
        adj[i][j.second] = adj[j.second][i];
        paths[i].push_back({j.second,1});
        paths[j.second].push_back({i,1});
      }
    }
    if (b>2){
      for (pair<short,short> j:xs[b-2]){
        if (adj[i][j.second]) continue;
        adj[i][j.second] = adj[j.second][i];
        paths[i].push_back({j.second,1});
        paths[j.second].push_back({i,1});
      }
    }
    if (b<m-1){
      for (pair<short,short> j:xs[b+2]){
        if (adj[i][j.second]) continue;
        adj[i][j.second] = adj[j.second][i];
        paths[i].push_back({j.second,1});
        paths[j.second].push_back({i,1});
      }
    }
    for (pair<short,short> j:ys[a]){
      if (adj[i][j.second]) continue;
      adj[i][j.second] = adj[j.second][i];
      if (abs(j.first-b)==1){
        paths[i].push_back({j.second,0});
        paths[j.second].push_back({i,0});
      }else{
        paths[i].push_back({j.second,1});
        paths[j.second].push_back({i,1});
      }
    }
    if (a>1){
      for (pair<short,short> j:ys[a-1]){
        if (adj[i][j.second]) continue;
        adj[i][j.second] = adj[j.second][i];
        paths[i].push_back({j.second,1});
        paths[j.second].push_back({i,1});
      }
    }
    if (a<n){
      for (pair<short,short> j:ys[a+1]){
        if (adj[i][j.second]) continue;
        adj[i][j.second] = adj[j.second][i];
        paths[i].push_back({j.second,1});
        paths[j.second].push_back({i,1});
      }
    }
    if (a>2){
      for (pair<short,short> j:ys[a-2]){
        if (adj[i][j.second]) continue;
        adj[i][j.second] = adj[j.second][i];
        paths[i].push_back({j.second,1});
        paths[j.second].push_back({i,1});
      }
    }
    if (a<n-1){
      for (pair<short,short> j:ys[a+2]){
        if (adj[i][j.second]) continue;
        adj[i][j.second] = adj[j.second][i];
        paths[i].push_back({j.second,1});
        paths[j.second].push_back({i,1});
      }
    }
    xs[b].push_back({a,i});
    ys[a].push_back({b,i});
  }
  queue<short> q;
  q.push(ind);
  ans[ind] = 0;
  while (!q.empty()){
    c = q.front();
    q.pop();
    checked[c] = 0;
    for (pair<short,short> i:paths[c]){
      if (ans[i.first]>ans[c]+i.second){
        ans[i.first] = ans[c]+i.second;
        if (!checked[i.first]){
          checked[i.first] = 1;
          q.push(i.first);
        }
      }
    }
    if (abs(pts[c].first-n)<=1||abs(pts[c].second-m)<=1){
      ans[c]++;
      res = min(res,ans[c]);
      ans[c]--;
    }
    if (pts[c].first==n&&pts[c].second==m){
      res = min(res,ans[c]);
    }
  }
  if (res!=10001) printf("%hu\n",res);
  else printf("-1\n");
}
