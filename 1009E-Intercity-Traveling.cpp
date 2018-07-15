#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
  ll N;
  scanf("%lld",&N);
  ll nums[N];
  ll ans = 0;
  ll mod = 998244353;
  ll cur = 1;
  ll cnt = 1;
  for (int i=0;i<N;i++){
    scanf("%lld",&nums[i]);
  }
  for (int i=N-1;i>=0;i--){
    ans = (ans+nums[i]*cur)%mod;
    cur = (cur*2+cnt)%mod;
    cnt = (cnt*2)%mod;
  }
  printf("%lld\n",ans%mod);
}
