#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long

int main() {
  int n;
  ll a,b,c,lo,hi,mid;
  scanf("%d",&n);
  for (int i=0;i<n;i++){
    scanf("%llu %llu",&a,&b);
    c = a*b;
    lo = 0;
    hi = 1000000;
    while (lo<hi){
      mid = (lo+hi)/2;
      if (mid*mid*mid<c) lo = mid+1;
      else hi = mid;
    }
    if (lo*lo*lo==c&&!(a%lo)&&!(b%lo)) printf("Yes\n");
    else printf("No\n");
  }
}
