#include <bits/stdc++.h>
using namespace std;

int main() {
  int n,a;
  scanf("%d",&n);
  int cnt = 1;
  int ans = 0;
  char q[10];
  stack<int> s;
  for (int i=0;i<n*2;i++){
    scanf("%s",q);
    if (q[0]=='a'){
      scanf("%d",&a);
      s.push(a);
    }else{
      if (!s.empty()&&s.top()==cnt){
        s.pop();
      }else{
        if (!s.empty()&&s.top()!=cnt){
          ans++;
          while (!s.empty()) s.pop();
        }
      }
      cnt++;
    }
  }
  printf("%d\n",ans);
}
