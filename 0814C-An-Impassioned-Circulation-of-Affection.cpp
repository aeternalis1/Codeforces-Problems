#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
  int n,cur;
  scanf("%d",&n);
  char s[n+1];
  scanf("%s",s);
  int dp[n+1][26];
  int ans[n+1][26];
  memset(dp,9999999,sizeof dp);
  for (int i=0;i<26;i++) dp[0][i] = 0;
  memset(ans,0,sizeof ans);
  for (int i=0;i<26;i++){
    for (int j=1;j<=n;j++){
      cur = 0;
      for (int k=0;k<j;k++){
        if (i!=s[k]-'a'){
          cur++;
        }
      }
      dp[j][i] = min(cur,dp[j][i]);
      for (int k=0;k<n-j;k++){
        if (i!=s[j+k]-'a') cur++;
        if (i!=s[k]-'a') cur--;
        dp[j][i] = min(cur,dp[j][i]);
      }
    }
  }
  for (int i=0;i<=n;i++){
    for (int j=0;j<26;j++){
      ans[dp[i][j]][j] = i;
    }
  }
  for (int i=0;i<n;i++){
    for (int j=0;j<26;j++){
      ans[i+1][j] = max(ans[i+1][j],ans[i][j]);
    }
  }
  int q,a;
  char b;
  scanf("%d",&q);
  for (int i=0;i<q;i++){
    scanf("%d %c",&a,&b);
    printf("%d\n",ans[a][b-'a']);
  }
}
