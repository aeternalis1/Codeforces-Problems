#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main() {
  int n,q;
  ll a,cnt;
  scanf("%d %d",&n,&q);
  int arr[35];
  int took[35];
  int need[35];
  memset(arr,0,sizeof arr);
  ll vals[35];
  cnt = 1;
  for (int i=0;i<35;i++){
    vals[i] = cnt;
    cnt *= 2;
  }
  for (int i=0;i<n;i++){
    scanf("%lld",&a);
    cnt = 0;
    while (a){
      a/=2;
      cnt++;
    }
    arr[cnt-1]++;
  }
  for (int i=0;i<q;i++){
    scanf("%lld",&a);
    for (int j=0;j<35;j++){
      need[j] = 0;
      took[j] = 0;
    }
    cnt = 0;
    while (a){
      need[cnt] = a%2;
      a /= 2;
      cnt++;
    }
    int ans = 0;
    int found = 1;
    for (int j=34;j>=0;j--){
      if (need[j]){
        if (arr[j]-took[j]){
          took[j]++;
          ans++;
        }else{
          ll tar = vals[j];
          for (int k=j-1;k>=0;k--){
            if ((arr[k]-took[k])*vals[k]>=tar){
              took[k] += tar/vals[k];
              ans += tar/vals[k];
              tar = 0;
              break;
            }else{
              tar -= (arr[k]-took[k])*vals[k];
              ans += arr[k]-took[k];
              took[k] = arr[k];
            }
          }
          if (tar){
            found = 0;
            break;
          }
        }
      }
    }
    if (found){
      printf("%d\n",ans);
    }else{
      printf("-1\n");
    }
  }
}
