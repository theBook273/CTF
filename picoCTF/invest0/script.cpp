#include <bits/stdc++.h>

using namespace std;

signed main() {
  freopen("flag.txt", "r", stdin);
  string temp;
  cin >> temp;
  for (int i = 0; i <= 5; i++) {
    cout << temp[i];
  }
  for (int i = 6; i < 15; i++) {
    cout << char(temp[i] - 5);
  }
  cout << char(temp[15] + 3);
  for (int i = 16; i < 26; i++) {
    cout << temp[i];
  }
}
