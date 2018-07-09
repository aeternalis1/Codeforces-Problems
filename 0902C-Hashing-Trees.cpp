#include <bits/stdc++.h>
using namespace std;
#define MAXN 100005

int main() {
  int n,tot=0;
  scanf("%d",&n);
  int arr[n+1];
  for (int i=0;i<=n;i++){
    scanf("%d",&arr[i]);
    tot += arr[i];
  }
  bool found = 0;
  for (int i=0;i<n;i++){
    if (arr[i]>1&&arr[i+1]>1) found = 1;
  }
  if (!found){
    printf("perfect\n");
    return 0;
  }
  printf("ambiguous\n");
  int ans[tot];
  ans[0] = 0;
  queue<int> q;
  q.push(0);
  int cur = 1, ind = 1, c;
  while (cur < tot){
    c = q.front();
    while (!q.empty()) q.pop();
    for (int i=cur;i<cur+arr[ind];i++){
      ans[i] = c+1;
      q.push(i);
    }
    cur += arr[ind];
    ind++;
  }
  for (int i=0;i<tot;i++) printf("%d ",ans[i]);
  printf("\n");
  cur = 1;
  ind = 1;
  queue<int> temp;
  while (!q.empty()) q.pop();
  q.push(0);
  while (cur < tot){
    for (int i=cur;i<cur+arr[ind];i++){
      if (!q.empty()){
        c = q.front();
        q.pop();
      }
      ans[i] = c+1;
      temp.push(i);
    }
    while (!q.empty()) q.pop();
    while (!temp.empty()){
      q.push(temp.front());
      temp.pop();
    }
    cur += arr[ind];
    ind++;
  }
  for (int i=0;i<tot;i++) printf("%d ",ans[i]);
  printf("\n");
}
