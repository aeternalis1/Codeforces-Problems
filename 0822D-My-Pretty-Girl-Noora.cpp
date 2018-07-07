#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define MAXN 50001

int main(){
  ll t,l,r;
  ll mod = 1e9+7;
  scanf("%lld %lld %lld",&t,&l,&r);
  ll dp[MAXN];
  ll rem[MAXN];
  bool prime[MAXN];
  vector<ll> primes;
  for (ll i=0;i<MAXN;i++) dp[i] = prime[i] = 0;
  for (ll i=2;i<MAXN;i++) rem[i] = i;
  for (ll i=2;i<MAXN;i++){
    if (!prime[i]){
      dp[i] = (i*(i-1)/2)%mod;
      primes.push_back(i);
      for (ll j=i+i;j<MAXN;j+=i){
        prime[j] = 1;
      }
    }
  }
  for (ll i:primes){
    for (ll j=i+i;j<MAXN;j+=i){
      while (rem[j]%i==0){
        dp[j] += (dp[i]*(rem[j]/i))%mod;
        rem[j] /= i;
      }
    }
  }
  ll cur = 1;
  ll ans = 0;
  for (ll i=0;i<r-l+1;i++){
    ans += (cur*dp[l+i])%mod;
    ans %= mod;
    cur = (cur*t)%mod;
  }
  printf("%lld\n",ans);
}
