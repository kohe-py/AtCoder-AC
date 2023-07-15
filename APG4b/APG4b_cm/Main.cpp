#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  // ここにプログラムを追記
  string a, b;
  int i, j;
  i = 0;
  j = 0;
  while (i < A){
    a.append("]");
    i ++;
  }
  while (j < B){
    b.append("]");
    j ++;
  }
  cout << "A:" << a << endl;
  cout << "B:" << b << endl;
}