#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long

int main(){
  int n;
  scanf("%d",&n);
  ll arr[n];
  pair<ll,int> a,b;
  priority_queue<pair<ll,int>,vector<pair<ll,int>>,greater<pair<ll,int>>> pq;
  unordered_map<ll,int> inds;
  for (int i=0;i<n;i++){
    scanf("%lld",&arr[i]);
    pq.push({arr[i],i});
  }
  ll ans[n];
  memset(ans,0,sizeof ans);
  int cnt;
  while (!pq.empty()){
    a = pq.top();
    pq.pop();
    if (!pq.empty()&&pq.top().first==a.first){
      pq.push({a.first<<1,pq.top().second});
      pq.pop();
    }else{
      ans[a.second] = a.first;
      cnt++;
    }
  }
  printf("%d\n",cnt);
  for (ll i: ans) if (i) printf("%lld ",i);
}
