#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main() {
  int n,k;
  scanf("%d %d",&n,&k);
  ll arr[n];
  ll ans[n];
  pair<ll,ll> cur;
  long long tot=0;
  priority_queue<pair<ll,ll>> pq;
  for (int i=0;i<n;i++){
    scanf("%lld",&arr[i]);
    if (i<k) pq.push({arr[i],i});
  }
  for (int i=k;i<k+n;i++){
    if (i<n) pq.push({arr[i],i});
    cur = pq.top();
    pq.pop();
    tot += cur.first*(i-cur.second);
    ans[cur.second] = i;
  }
  printf("%lld\n",tot);
  for (ll i:ans) printf("%d ",i+1);
}
