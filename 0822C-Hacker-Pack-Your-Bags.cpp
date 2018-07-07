#include <bits/stdc++.h>
using namespace std;

struct seg{
  int a,b,c,d;
  bool operator<(const seg&s){
    if (s.a==a) return s.b > b;
    return s.a > a;
  }
};

int main(){
  int n,X,a,b,c;
  scanf("%d %d",&n,&X);
  seg arr[n*2];
  int checked[200001];
  for (int i=0;i<200001;i++){
    checked[i] = 0;
  }
  for (int i=0;i<n;i++){
    scanf("%d %d %d",&a,&b,&c);
    arr[(i<<1)].a = a;
    arr[(i<<1)].b = 0;
    arr[(i<<1)].c = c;
    arr[(i<<1)].d = b-a+1;
    arr[(i<<1)+1].a = b;
    arr[(i<<1)+1].b = 1;
    arr[(i<<1)+1].c = c;
    arr[(i<<1)+1].d = b-a+1;
  }
  sort(arr,arr+n*2);
  int ans = 2000000001;
  for (int i=0;i<n*2;i++){
    if (!arr[i].b){
      if (X-arr[i].d>=0&&checked[X-arr[i].d]){
        ans = min(ans,checked[X-arr[i].d]+arr[i].c);
      }
    }else{
      if (!checked[arr[i].d]||checked[arr[i].d]>arr[i].c){
        checked[arr[i].d] = arr[i].c;
      }
    }
  }
  if (ans != 2000000001){
    printf("%d\n",ans);
  }else{
    printf("-1\n");
  }
}
