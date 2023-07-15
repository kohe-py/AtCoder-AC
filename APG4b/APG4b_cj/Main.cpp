#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  int ave = 0;
  vector<int> vec(N);
  for (int i = 0; i < N; i++){
    cin >> vec.at(i);
    ave += vec.at(i);
  }
  ave /= N;
  for (int i = 0; i < N; i++){
    if (vec.at(i) > ave){
        cout << vec.at(i) - ave << endl;
    }
    else{
        cout << ave - vec.at(i) << endl;
    }
  }
}