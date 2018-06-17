#include <bits/stdc++.h>
using namespace std;

struct seg{
  int l,r,i;
  bool operator<(const seg&s){
    if (s.l==l) return s.r < r;
    return s.l > l;
  }
};

int main(){
  int n,a,b;
  scanf("%d",&n);
  seg arr[n];
  for (int i=0;i<n;i++){
    scanf("%d %d",&arr[i].l,&arr[i].r);
    arr[i].i = i+1;
  }
  sort(arr,arr+n);
  int cur = 1;
  int ind = arr[0].i;
  int r = arr[0].r;
  while (cur<n){
    if (arr[cur].r<=r){
      printf("%d %d\n",arr[cur].i,ind);
      return 0;
    }
    if (arr[cur].r>=r){
      r = arr[cur].r;
      ind = arr[cur].i;
    }
    cur++;
  }
  printf("-1 -1\n");
}
