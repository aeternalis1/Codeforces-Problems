#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
typedef long long ll;
#define f first
#define s second
const ll mod = 1e9+7;

int main(){
    int prime[MAXN], arr[MAXN];
    vector<int> primes, taken;
    vector<int> nodes[MAXN], paths[MAXN];
    memset(prime,0,sizeof prime);
    for (int i=2;i<MAXN;i++){
        if (!prime[i]){
            primes.push_back(i);
            for (int j=i+i;j<MAXN;j+=i){
                prime[j] = 1;
            }
        }
    }
    int N,a,b,c,ind,res;
    scanf("%d",&N);
    for (int i=0;i<N;i++){
        scanf("%d",&arr[i]);
        a = arr[i];
        for (int j:primes){
            if (arr[i]%j==0){
                nodes[j].push_back(i);
            }
            while (a%j==0) a/=j;
            if (j>sqrt(a)){
                nodes[a].push_back(i);
                break;
            }
        }
    }
    for (int i=0;i<N-1;i++){
        scanf("%d %d",&a,&b);
        a--;
        b--;
        paths[a].push_back(b);
        paths[b].push_back(a);
    }
    queue<int> q;
    int chk[MAXN], seen[MAXN];
    memset(chk,0,sizeof chk);
    memset(seen,0,sizeof seen);
    int ans = 0;
    for (int i:primes){
        if (nodes[i].size()){
            for (int k:nodes[i]){
                if (seen[k]){
                    continue;
                }
                taken.clear();
                q.push(k);
                taken.push_back(k);
                chk[k] = 1;
                while (!q.empty()){
                    c = q.front();
                    q.pop();
                    for (int j:paths[c]){
                        if (!chk[j]&&arr[j]%i==0){
                            chk[j] = chk[c]+1;
                            q.push(j);
                            taken.push_back(j);
                        }
                    }
                }
                ind = 0;
                res = 0;
                for (int j:taken){
                    if (chk[j]>res){
                        res = chk[j];
                        ind = j;
                    }
                    chk[j] = 0;
                }
                chk[ind] = 1;
                q.push(ind);
                while (!q.empty()){
                    c = q.front();
                    q.pop();
                    for (int j:paths[c]){
                        if (!chk[j]&&arr[j]%i==0){
                            chk[j] = chk[c]+1;
                            q.push(j);
                        }
                    }
                }
                ind = 0;
                res = 0;
                for (int j:taken){
                    if (chk[j]>res){
                        res = chk[j];
                        ind = j;
                    }
                    chk[j] = 0;
                }
                chk[ind] = 1;
                q.push(ind);
                while (!q.empty()){
                    c = q.front();
                    q.pop();
                    for (int j:paths[c]){
                        if (!chk[j]&&arr[j]%i==0){
                            chk[j] = chk[c]+1;
                            q.push(j);
                        }
                    }
                }
                res = 0;
                for (int j:taken){
                    res = max(res,chk[j]);
                    chk[j] = 0;
                    seen[j] = 1;
                }
                ans = max(ans,res);
            }
            for (int k:nodes[i]){
                seen[k] = 0;
            }
        }
    }
    printf("%d\n",ans);
}
