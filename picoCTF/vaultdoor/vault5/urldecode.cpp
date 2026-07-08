#include <bits/stdc++.h>

using namespace std;

signed main() {
  string res;
  string a;
  cin >> a;
  for (int i = 0; i < a.size(); i++) {
    if (a[i] == '%') {
      string temp;
      i++;
      while (a[i] != '%') {
        temp.push_back(a[i]);
        i++;
        if (i >= a.size()) {
          break;
        }
      }
      res.push_back(stoi(temp, nullptr, 16));
      i--;
    }
  }
  cout << "picoCTF{" << res << "}" << endl;
}
