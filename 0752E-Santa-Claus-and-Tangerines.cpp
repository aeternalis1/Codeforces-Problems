#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000001;
const int MAXC = 10000001;
typedef long long ll;
#define f first
#define s second

int arr[MAXN], dp[MAXC];

int solve(int cur, int tar){
    if (dp[cur]!=-1) return dp[cur];
    if (cur<tar||!cur) return dp[cur] = 0;
    if (cur==tar) return dp[cur] = 1;
    dp[cur] = solve(cur>>1,tar)+solve((cur>>1)+(cur&1),tar);
    if (!dp[cur]) return dp[cur] = 1;
    else return dp[cur];
}

int chk(int cur, int tar, int N){
    if (!cur) return 0;
    memset(dp,-1,sizeof dp);
    for (int i=0;i<N;i++){
        tar -= solve(arr[i],cur);
        if (tar<=0) return 1;
    }
    return 0;
}

int main(){
    int N,K;
    scanf("%d %d",&N,&K);
    for (int i=0;i<N;i++){
        scanf("%d",&arr[i]);
    }
    sort(arr,arr+N);
    int lo = 0, hi = 1e8, mid;
    while (lo<hi){
        mid = (lo+hi)/2;
        if (chk(mid,K,N)){
            lo = mid+1;
        }else{
            hi = mid;
        }
    }
    printf("%d\n",lo-1);
}

