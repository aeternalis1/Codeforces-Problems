#include <bits/stdc++.h>
using namespace std;

#define ll long long

int gcd(int a, int b){
  if (!a) return b;
  if (!b) return a;
  if (a%b==0) return b;
  return gcd(b,a%b);
}

int main(){
  int N,m;
  scanf("%d %d",&N,&m);
  int edge = 0;
  vector<pair<int,int>> ans;
  for (int i=1;i<=N;i++){
    if (i==1){
      for (int j=2;j<=N;j++){
        edge++;
        ans.push_back({1,j});
        if (edge==m){
          break;
        }
      }
    }else if(i%2==0){
      for (int j=3;j<=N;j+=2){
        if (gcd(i,j)==1){
          edge++;
          ans.push_back({i,j});
          if (edge==m){
            break;
          }
        }
      }
    }else{
      for (int j=i+2;j<=N;j+=2){
        if (gcd(j,i)==1){
          edge++;
          ans.push_back({i,j});
          if (edge==m){
            break;
          }
        }
      }
    }
    if (edge==m) break;
  }
  if (edge==m&&m>=N-1){
    printf("Possible\n");
    for (pair<int,int> i:ans){
      printf("%d %d\n",i.first,i.second);
    }
  }else{
    printf("Impossible\n");
  }
}
