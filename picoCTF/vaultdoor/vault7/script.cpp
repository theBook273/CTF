#include <bits/stdc++.h>
#define int long long

using namespace std;

int a[] = {1096770097, 1952395366, 1600270708, 1601398833,
           1716808014, 1734292070, 825440356,  858796849};

string toBin(int x) {
  string s;
  while (x) {
    if (x % 2 == 1) {
      s.push_back('1');
    } else {
      s.push_back('0');
    }
    x /= 2;
  }
  if (s.size() < 32) {
    s.append(32 - s.size(), '0');
  }
  reverse(s.begin(), s.end());
  return s;
}

char toHex(string x) {
  int res = 0, dem = 7;
  for (int i = 0; i < 8; i++) {
    res += (x[i] - '0') * pow(2, dem);
    dem--;
  }
  return char(res);
}

string word;

void solve(int x) {
  string temp = toBin(x);
  string charInHex = "";
  for (int i = 1; i <= 32; i++) {
    charInHex.push_back(temp[i - 1]);
    if (i % 8 == 0) {
      word.push_back(toHex(charInHex));
      charInHex = "";
    }
  }
}

signed main() {
  for (auto &i : a) {
    solve(i);
  }
  cout << "picoCTF{" << word << "}" << "\n";
};
