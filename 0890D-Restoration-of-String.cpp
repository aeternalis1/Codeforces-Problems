#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  string s;
  cin >> N;
  int next[26];
  int last[26];
  bool need[26];
  bool exist[26];
  for (int i=0;i<26;i++){
    next[i] = last[i] = -1;
    need[i] = false;
  }
  for (int i=0;i<N;i++){
    cin >> s;
    memset(exist,false,sizeof exist);
    for (int j=0;j<s.length();j++){
      need[s[j]-'a'] = true;
      if (exist[s[j]-'a']){
        printf("NO");
        return 0;
      }
      exist[s[j]-'a'] = true;
      if (j!=0){
        if ((next[s[j-1]-'a']!=-1&&next[s[j-1]-'a']!=s[j]-'a')||(last[s[j]-'a']!=-1&&last[s[j]-'a']!=s[j-1]-'a')){
          printf("NO");
          return 0;
        }
        int temp = s[j]-'a';
        int temp2 = s[j-1]-'a';
        next[s[j-1]-'a'] = temp;
        last[s[j]-'a'] = temp2;
      }
    }
  }
  vector<int> valid;
  vector<int> seq;
  for (int i=0;i<26;i++){
    if (last[i]==-1&&need[i]){
      valid.push_back(i);
    }
  }
  if (!valid.size()){
    printf("NO");
    return 0;
  }
  for (int i=0;i<valid.size();i++){
    int cur = valid[i];
    seq.push_back(cur);
    while (next[cur]!=-1){
      cur = next[cur];
      seq.push_back(cur);
    }
  }
  memset(exist,false,sizeof exist);
  for (int i=0;i<seq.size();i++){
    if (exist[seq[i]]){
      printf("NO");
      return 0;
    }
    exist[seq[i]] = true;
  }
  for (int i=0;i<26;i++){
    if (!exist[i]&&need[i]){
      printf("NO");
      return 0;
    }
  }
  for (int i=0;i<seq.size();i++){
    printf("%c",seq[i]+'a');
  }
  printf("\n");
  return 0;
}
