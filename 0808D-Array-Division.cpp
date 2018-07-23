#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
  int N;
  scanf("%d",&N);
  ll nums[N];
  ll pre[N+1];
  ll suf[N+1];
  map<ll,bool> avail;
  map<ll,bool> avail2;
  for (int i=0;i<N;i++){
    scanf("%lld",&nums[i]);
  }
  pre[0] = 0;
  suf[N] = nums[N-1];
  bool f = 0;
  for (int i=0;i<N;i++){
    pre[i+1] = pre[i]+nums[i];
  }
  for (int i=N-1;i>0;i--){
    suf[i] = suf[i+1]+nums[i-1];
  }
  for (int i=1;i<N;i++){
    avail[nums[i-1]] = 1;
    if (pre[i]==suf[i+1]){
      f = 1;
    }
    else if ((pre[i]-suf[i+1])%2==0&&avail[(pre[i]-suf[i+1])/2]){
      f = 1;
    }
  }
  for (int i=N;i>0;i--){
    avail2[nums[i-1]] = 1;
    if (pre[i-1]==suf[i]){
      f = 1;
    }
    else if ((suf[i]-pre[i-1])%2==0&&avail2[(suf[i]-pre[i-1])/2]){
      f = 1;
    }
  }
  if (f) printf("YES\n");
  else printf("NO\n");
}
