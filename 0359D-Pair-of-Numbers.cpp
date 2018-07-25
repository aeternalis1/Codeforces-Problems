#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
  int n,cur,ans=0,l,r,f;
  scanf("%d",&n);
  int nums[n];
  vector<int> inds;
  pair<int,int> arr[n];
  int cnt=0;
  for (int i=0;i<n;i++){
    scanf("%d",&nums[i]);
    arr[i] = {nums[i],i};
  }
  sort(arr,arr+n);
  for (int i=0;i<n;i++){
    cur = arr[i].first;
    l = arr[i].second;
    r = arr[i].second;
    f = 0;
    while (l>=0&&nums[l]%cur==0){
      cnt++;
      l--;
      if (l>=0&&cur%nums[l]==0){
        f = 1;
        break;
      }
    }
    if (!f){
      while (r<n&&nums[r]%cur==0){
        cnt++;
        r++;
      }
    }
    if (r-l>ans){
      ans = r-l;
      inds.clear();
      inds.push_back(l);
    }else if(r-l==ans){
      inds.push_back(l);
    }
  }
  printf("%d %d\n",inds.size(),ans-2);
  sort(inds.begin(),inds.end());
  for (int i:inds){
    printf("%d ",i+2);
  }
}
