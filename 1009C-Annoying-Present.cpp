#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
  ll n,m,x,d;
  ll ans = 0;
  ll cur;
  scanf("%lld %lld",&n,&m);
  if (n%2) cur = n/2*(n/2+1);
  else cur = n/2*(n/2+1)-n/2;
  for (int i=0;i<m;i++){
    scanf("%lld %lld",&x,&d);
    ans += x*n;
    if (d>=0) ans += d*(n*(n-1)/2);
    else ans += d*cur;
  }
  printf("%.9lf\n",(double)ans/n);
}
