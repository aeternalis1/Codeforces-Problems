#include <bits/stdc++.h>
using namespace std;

int main(){
  int n,m,a,b;
  scanf("%d %d",&n,&m);
  int nums[n];
  int ans[n];
  for (int i=0;i<n;i++){
    scanf("%d",&nums[i]);
    ans[i] = i;
  }
  int cur = 0;
  int l = 0;
  int same = -1;
  for (int i=1;i<n;i++){
    if (nums[i]<nums[i-1]&&!cur){
      cur = 1;
    }else if (nums[i]>nums[i-1]&&cur){
      for (int j=l;j<i;j++){
        ans[j] = i-1;
      }
      cur = 0;
      l = i-1;
      if (same!=-1&&nums[i-1]==nums[same]){
        l = same;
      }
    }else if(nums[i]==nums[i-1]&&cur){
      if (same==-1) same = i-1;
    }
    if (nums[i] != nums[i-1]) same = -1;
  }
  for (int j=l;j<n;j++){
    ans[j] = n-1;
  }
  for (int i=0;i<m;i++){
    scanf("%d %d",&a,&b);
    if (ans[a-1]>=b-1) printf("Yes\n");
    else printf("No\n");
  }
}
