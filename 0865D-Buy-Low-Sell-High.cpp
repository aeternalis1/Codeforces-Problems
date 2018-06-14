#include <bits/stdc++.h>
using namespace std;

int main(){
  int N,a;
  long long ans = 0;
  scanf("%d",&N);
  priority_queue<int,vector<int>,greater<int>> pq;
  for (int i=0;i<N;i++){
    scanf("%d",&a);
    if (!i){
      pq.push(a);
      continue;
    }
    if (pq.top()<a){
      ans += a-pq.top();
      pq.pop();
      pq.push(a);
    }
    pq.push(a);
  }
  printf("%lld\n",ans);
}
