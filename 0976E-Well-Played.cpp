#include <bits/stdc++.h>
using namespace std;

struct dude{
  int h,d,v;
  bool operator<(const dude&d){
    return d.v < v;
  }
};

int main(){
  int n,a,b;
  scanf("%d %d %d",&n,&a,&b);
  dude arr[n];
  bool taken[n];
  memset(taken,0,sizeof taken);
  long long ans = 0, ans1 = 0, ans2 = 0, ans3 = 0;
  long long cur = pow(2,a), res, temp;
  for (int i=0;i<n;i++){
    scanf("%d %d",&arr[i].h,&arr[i].d);
    arr[i].v = arr[i].h-arr[i].d;
    ans += arr[i].d;
  }
  if (!b){
    printf("%lld\n",ans);
    return 0;
  }
  sort(arr,arr+n);
  for (int i=0;i<min(n,b);i++){
    if (arr[i].v<0) break;
    if (i!=b-1) ans1 += arr[i].v;
    ans2 += arr[i].v;
    taken[i] = 1;
  }
  for (int i=0;i<n;i++){
    if (taken[i]) res = ans2-arr[i].v;
    else res = ans1;
    temp = cur*arr[i].h-arr[i].d;
    ans3 = max(ans3,res+temp);
  }
  printf("%lld\n",ans+ans3);
}
