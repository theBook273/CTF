#include <bits/stdc++.h>
#define int long long

using namespace std;

signed main() {
  string s = "ZGSOCXPQUYHMILERVTBWNAFJDK";
  string res = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  string decode;
  map<char, char> translator;

  for (int i = 0; i < s.size(); i++) {
    translator[s[i]] = res[i];
  }

  getline(cin, decode, '|');

  for (auto &i : decode) {
    if (translator.count(i)) {
      i = translator[i];
    } else if (translator.count(toupper(i))) {
      i = tolower(translator[toupper(i)]);
    }
  }

  cout << decode << endl;
}
