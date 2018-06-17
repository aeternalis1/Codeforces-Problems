#include <bits/stdc++.h>
using namespace std;

#define MAXN 100001
vector<int> dep[MAXN];
int nums[MAXN];
bool cop[MAXN];
bool checked[MAXN];
queue <int> q1;
queue <int> q2;

int main(){
  int N,M;
  scanf("%d %d",&N,&M);
  int a,b;
  for (int i=0;i<N;i++){
    nums[i] = checked[i] = 0;
  }
  for (int i=0;i<N;i++){
    scanf("%d",&cop[i]);
  }
  for (int i=0;i<M;i++){
    scanf("%d %d",&a,&b);
    nums[a]++;
    dep[b].push_back(a);
  }
  for (int i=0;i<N;i++){
    if (nums[i]==0){
      if (cop[i]){
        q2.push(i);
      }else{
        q1.push(i);
      }
    }
  }
  int cur;
  int ans = 0;
  while (!q1.empty()||!q2.empty()){
    while (!q1.empty()){
      cur = q1.front();
      q1.pop();
      if (checked[cur]) continue;
      checked[cur] = true;
      for (int i:dep[cur]){
        nums[i]--;
        if (nums[i]==0){
          if (cop[i]){
            q2.push(i);
          }
          else q1.push(i);
        }
      }
    }
    if (!q2.empty()) ans++;
    while (!q2.empty()){
      cur = q2.front();
      q2.pop();
      if (checked[cur]) continue;
      checked[cur] = true;
      for (int j:dep[cur]){
        nums[j]--;
        if (nums[j]==0){
          if (!cop[j]){
            q1.push(j);
          }else{
            q2.push(j);
          }
        }
      }
    }
  }
  printf("%d",ans);
}
