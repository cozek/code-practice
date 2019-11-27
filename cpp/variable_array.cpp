#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
  int num_arrays, num_queries;
  scanf("%d %d",&num_arrays, &num_queries );

  int num,size;
  std::vector<std::vector<int> > bigV;
  std::vector<int> v;

  for (int arr = 0; arr < num_arrays; arr++){
    cin >> size;
    for (int i =0 ; i<size; i++) {
      cin >> num;
      v.push_back(num);
    }
    bigV.push_back(v);
    v.clear();
  }

  int q1,q2;
  for (int q=0; q<num_queries; q++) {
    cin >> q1;
    cin >> q2;
    cout << bigV[q1][q2] << endl;
  }

}