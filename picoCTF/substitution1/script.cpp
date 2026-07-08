#include <bits/stdc++.h>

using namespace std;

signed main() {
  string a = "--NF----R-----Q----Z------";
  string b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  string decode;
  map<char, char> translator;

  for (int i = 0; i < a.size(); i++) {
    translator[a[i]] = b[i];
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
