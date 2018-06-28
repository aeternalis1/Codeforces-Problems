#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long

struct seg{
  ll a,b;
  bool operator<(const seg&s){
    if (a==s.a) return b<s.b;
    return a < s.a;
  }
};

int main(){
  int n,a,b,peak;
  scanf("%d",&n);
  seg arr[n*2];
  ll ans[n+1];
  memset(ans,0,sizeof ans);
  unordered_map<ll,int> checked;
  for (int i=0;i<n;i++){
    scanf("%llu %llu",&arr[i*2].a,&arr[i*2+1].a);
    arr[i*2].b = 0;
    arr[i*2+1].b = 1;
  }
  sort(arr,arr+n*2);
  ll last = arr[0].a;
  int cnt = 0;
  for (int i=0;i<n*2;i++){
    int old = cnt;
    peak = cnt;
    if (arr[i].b) cnt--;
    else cnt++;
    peak = max(peak,cnt);
    while (i<n*2-1&&arr[i].a==arr[i+1].a){
      if (!arr[i+1].b) cnt++;
      else cnt--;
      i++;
      peak = max(peak,cnt);
    }
    ans[peak]++;
    ans[old] += arr[i].a-last-1;
    last = arr[i].a;
  }
  for (int i=1;i<=n;i++){
    printf("%llu ",ans[i]);
  }
}
