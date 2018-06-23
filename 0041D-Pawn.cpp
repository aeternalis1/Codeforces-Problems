#include <bits/stdc++.h>
using namespace std;

int main(){
  int n,m,k;
  char c;
  scanf("%d %d %d",&n,&m,&k);
  k++;
  int grid[n][m];
  int dp[n][m][k+1];
  memset(dp,-1,sizeof dp);
  int par[n][m][k+1];
  for (int i=0;i<n;i++){
    for (int j=0;j<m;j++){
      scanf(" %c",&c);
      grid[i][j] = c-'0';
    }
  }
  for (int i=n-1;i>=0;i--){
    for (int j=0;j<m;j++){
      if (i==n-1){
        dp[i][j][grid[i][j]%k]=grid[i][j];
        continue;
      }
      if (j>0){
        for (int l=0;l<k;l++){
          if (dp[i+1][j-1][l]==-1) continue;
          if (dp[i][j][(l+grid[i][j])%k]<dp[i+1][j-1][l]+grid[i][j]){
            dp[i][j][(l+grid[i][j])%k] = dp[i+1][j-1][l]+grid[i][j];
            par[i][j][(l+grid[i][j])%k] = 0;
          }
        }
      }
      if (j<m-1){
        for (int l=0;l<k;l++){
          if (dp[i+1][j+1][l]==-1) continue;
          if (dp[i][j][(l+grid[i][j])%k]<dp[i+1][j+1][l]+grid[i][j]){
            dp[i][j][(l+grid[i][j])%k] = dp[i+1][j+1][l]+grid[i][j];
            par[i][j][(l+grid[i][j])%k] = 1;
          }
        }
      }
    }
  }
  int ans = -1;
  int ind = 0;
  for (int i=0;i<m;i++){
    if (dp[0][i][0]>ans){
      ans = dp[0][i][0];
      ind = i;
    }
  }
  if (ans==-1){
    printf("-1\n");
    return 0;
  }
  char coms[n];
  int nxt = 0;
  for (int i=0;i<n-1;i++){
    if (!par[i][ind][nxt]){
      nxt = (dp[i][ind][nxt]-grid[i][ind])%k;
      ind--;
      coms[i] = 'R';
    }else{
      nxt = (dp[i][ind][nxt]-grid[i][ind])%k;
      ind++;
      coms[i] = 'L';
    }
  }
  printf("%d\n",ans);
  printf("%d\n",ind+1);
  for (int i=n-2;i>=0;i--){
    printf("%c",coms[i]);
  }
}
