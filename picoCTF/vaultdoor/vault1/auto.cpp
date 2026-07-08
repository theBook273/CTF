#include <bits/stdc++.h>

using namespace std;

signed main() {
  char a[32];
  freopen("temp.txt", "r", stdin);
  string temp;
  int index;
  char val;
  set<int> se;
  while (getline(cin, temp)) {
    if (temp == "") {
      break;
    }
    for (int i = 0; i < temp.size() - 1; i++) {
      if (temp[i] == '(') {
        i++;
        index = temp[i] - '0';
        i++;

        while (isalnum(temp[i])) {
          index = index * 10 + temp[i] - '0';
          i++;
        }
      }

      if (temp[i - 1] == '\'' && temp[i + 1] == '\'') {
        val = temp[i];
        break;
      }
    }
    if (!se.count(index)) {
      a[index] = val;
    }
    se.insert(index);
  }
  cout << "picoCTF{";
  for (auto &i : a) {
    cout << i;
  }
  cout << "}\n";
}
