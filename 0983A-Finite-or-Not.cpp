#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long

ll gcd(ll a, ll b){
  if (a%b==0) return b;
  return gcd(b,a%b);
}

int main(){
  ll n,a,b,c,d;
  //srand(time(NULL));
  scanf("%I64d",&n);
  for (int i=0;i<n;i++){
    scanf("%I64d %I64d %I64d",&a,&b,&c);
    //a = rand()%20;
    //b = rand()%20+1;
    //c = 2;
    //printf("%d %d %lf\n",a,b,(double)a/b);
    d = gcd(a,b);
    a /= d;
    b /= d;
    while (1){
      d = gcd(b,c);
      if (d==1) break;
      while (b%d==0) b /= d;
    }
    if (c%b==0||b%c==0||!a) printf("Finite\n");
    else printf("Infinite\n");
  }
}
