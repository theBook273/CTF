#include <bits/stdc++.h>

using namespace std;

string sam = "jU5t_a_sna_3lpm11g54e_u_4_m4r042";
char pass[32];

signed main() {
  int i = 0;
  for (; i < 8; i++) {
    pass[i] = sam[i];
  }
  for (; i < 16; i++) {
    pass[23 - i] = sam[i];
  }
  for (; i < 32; i += 2) {
    pass[46 - i] = sam[i];
  }
  for (i = 31; i >= 17; i -= 2) {
    pass[i] = sam[i];
  }
  cout << "picoCTF{";
  for (auto &i : pass) {
    cout << i;
  }
  cout << "}\n";
}
