#include <bits/stdc++.h>

using namespace std;

char s[] = {
    106,  85,   53,   116,  95,   52,   95,   98,   0x55, 0x6e, 0x43,
    0x68, 0x5f, 0x30, 0x66, 0x5f, 0142, 0131, 0164, 063,  0163, 0137,
    0145, 060,  '2',  '1',  '3',  '8',  '7',  '2',  '1',  '3',
};

signed main() {
  cout << "picoCTF{";
  for (auto &i : s) {
    cout << i;
  }
  cout << "}\n";
}
