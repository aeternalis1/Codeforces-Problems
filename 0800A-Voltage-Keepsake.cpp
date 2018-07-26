#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
  ll n,p;
  scanf("%lld %lld",&n,&p);
  ll arr[n][2];
  for (int i=0;i<n;i++){
    scanf("%lld %lld",&arr[i][0],&arr[i][1]);
  }
  double lo = 0;
  double hi = 1e10;
  double mid,cur;
  while (abs(hi-lo)>=0.00001){
    mid = (lo+hi)/2;
    cur = 0;
    for (int i=0;i<n;i++){
      if (arr[i][1]<arr[i][0]*mid){
        cur += (arr[i][0]*mid-arr[i][1])/p;
      }
    }
    if (cur>mid){
      hi = mid;
    }else{
      lo = mid;
    }
  }
  if (abs(lo-1e10)<=0.001) printf("-1\n");
  else printf("%.5lf\n",lo);
}
