#include <bits/stdc++.h>
using namespace std;

int main(){
  int N,M,K,l,r,ll,lr,ind;
  scanf("%d %d %d",&N,&M,&K);
  int choices[M+1];
  int dp[N+1][K+1];
  vector<int> pos;
  for (int i=0;i<=N;i++){
    for (int j=0;j<=K;j++){
      dp[i][j] = 999999;
    }
  }
  dp[0][0] = 0;
  char arr[M+1];
  for (int i=0;i<N;i++){
    scanf("%s",arr);
    for (int j=0;j<=M;j++){
      choices[j] = 999999;
    }
    pos.clear();
    for (int j=0;j<M;j++){
      if (arr[j]=='1'){
        pos.push_back(j);
      }
    }
    ind = pos.size();
    for (int j=0;j<ind;j++){
      for (int k=0;k<=j;k++){
        choices[j] = min(choices[j],abs(pos[k]-pos[ind-(j-k)-1])+1);
      }
    }
    choices[ind++] = 0;
    for (int j=0;j<=K;j++){
      for (int k=0;k<ind;k++){
        if (k+j>K) break;
        if (dp[i][j]+choices[k]<dp[i+1][j+k]){
          dp[i+1][j+k] = dp[i][j]+choices[k];
        }
      }
    }
  }
  int ans = 999999;
  for (int i=0;i<=K;i++){
    ans = min(ans,dp[N][i]);
  }
  printf("%d\n",ans);
}
