#include <bits/stdc++.h>

using namespace std;

signed main() {
  freopen("flag.txt", "r", stdin);
  string pic1, pic2, pic3;
  cin >> pic1 >> pic2 >> pic3;
  int dem1, dem2, dem3;
  dem1 = dem2 = dem3 = 0;

  cout << char(int(pic2[dem2]) - 21);
  dem2++;
  cout << char(pic3[dem3]);
  dem3++;
  cout << char(pic3[dem3]);
  dem3++;
  cout << char(pic2[dem2] - 4);
  dem1++;
  for (int i = 6; i < 10; i++) {
    cout << pic1[dem1];
    dem1++;
  }
  dem3++;
  for (int i = 10; i < 15; i++) {
    cout << pic3[dem3];
    dem3++;
  }
  for (int i = 15; i < 26; i++) {
    cout << pic1[dem1];
    dem1++;
  }
}
