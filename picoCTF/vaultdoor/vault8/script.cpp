#include <bits/stdc++.h>
#define int long long

using namespace std;
int expected[] = {0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4,
                  0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86,
                  0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xA4,
                  0xA4, 0xA4, 0xD1, 0xE1, 0xC2, 0xB4, 0xA4, 0xF1};

string toBin(int x) {
  string temps = "";
  int tempn = x;
  while (tempn) {
    temps.push_back((tempn & 1) + '0');
    tempn /= 2;
  }
  while (temps.size() < 8) {
    temps.push_back('0');
  }
  reverse(temps.begin(), temps.end());
  return temps;
}

int decode(string s) {
  swap(s[6], s[7]);
  swap(s[2], s[5]);
  swap(s[3], s[4]);
  swap(s[0], s[1]);
  swap(s[4], s[7]);
  swap(s[5], s[6]);
  swap(s[0], s[3]);
  swap(s[1], s[2]);
  return stoi(s, nullptr, 2);
}

signed main() {
  cout << "picoCTF{";
  for (auto &i : expected) {
    string temp = toBin(i);
    cout << char(decode(temp));
  }
  cout << "}\n";
}
