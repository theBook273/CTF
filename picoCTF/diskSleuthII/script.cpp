#include <bits/stdc++.h>

using namespace std;

signed main() {
  freopen("pass.txt", "r", stdin);
  string temp;
  while (getline(cin, temp)) {
    if (temp.find('(') != string::npos) {
      for (auto &i : temp) {
        if (i != ' ' && i != '(' && i != ')') {
          cout << i;
        }
      }
    }
  }
}
