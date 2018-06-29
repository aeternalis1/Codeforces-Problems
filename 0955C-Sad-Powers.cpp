#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long

int main(){
  ll a,b,c,d,l,r,lo,hi,mid;
  vector<ll> nums;
  ll big = 1e18;
  for (ll i=2;i<1000001;i++){
    ll cur = i*i*i;
    for (ll j=3;j<64;j++){
      if (cur>big||cur<0) break;
      if (pow((unsigned long long)pow(cur,0.5),2)!=cur){
        ll temp = (unsigned long long)pow(cur,0.5);
        lo = 0;
        hi = 1e9;
        while (lo<hi){
          mid = (lo+hi)/2;
          if (mid*mid<cur) lo = mid+1;
          else hi = mid;
        }
        if (lo*lo!=cur){
          nums.push_back(cur);
        }
      }
      if (big/i<=cur) break;
      cur *= i;
    }
  }
  sort(nums.begin(),nums.end());
  nums.erase(unique(nums.begin(), nums.end()),nums.end());
  int Q;
  ll top = nums.size();
  scanf("%d",&Q);
  for (int i=0;i<Q;i++){
    scanf("%llu %llu",&a,&b);
    lo = 0;
    hi = 1e9+1;
    while (lo<hi){
      l = (lo+hi)/2;
      if (l*l>=a) hi = l;
      else lo = l+1;
    }
    l = lo-1;
    lo = 0;
    hi = 1e9+1;
    while (lo<hi){
      r = (lo+hi)/2;
      if (r*r<=b) lo = r+1;
      else hi = r;
    }
    r = lo;
    lo = 0;
    hi = top;
    while (lo<hi){
      c = (lo+hi)/2;
      if (nums[c]<=b) lo = c+1;
      else hi = c;
    }
    c = lo;
    lo = 0;
    hi = top;
    while (lo<hi){
      d = (lo+hi)/2;
      if (nums[d]<a) lo = d+1;
      else hi = d;
    }
    d = lo;
    printf("%llu\n",r-l+c-d-1);
  }
}
