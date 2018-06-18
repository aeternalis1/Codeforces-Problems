#include <bits/stdc++.h>
using namespace std;

#define MAXN 1000001

int checked[MAXN];
int sums[MAXN][10];

int dfs(int cur){
  if (checked[cur]) return checked[cur];
  int res = 1, temp;
  while (cur){
    temp = cur%10;
    cur /= 10;
    if (temp) res *= temp;
  }
  if (res>=10) res = dfs(res);
  return checked[cur] = res;
}

int main(){
  for (int i=1;i<MAXN;i++){
    if (!checked[i]) sums[i][dfs(i)]++;
    for (int j=1;j<10;j++) sums[i][j] += sums[i-1][j];
  }
  int Q,l,r,k;
  scanf("%d",&Q);
  for (int i=0;i<Q;i++){
    scanf("%d %d %d",&l,&r,&k);
    printf("%d\n",sums[r][k]-sums[l-1][k]);
  }
}
