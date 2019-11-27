#include <string>
#include <iostream>
using namespace std;

string swap(string a, int len) {

  char temp = a[len-1];
  a[len-1] = a[0];
  a[0] = temp;

  return a;
}

int main() {
  string a,b;
  cin >> a;
  cin >> b;

  int len_a = a.size();
  int len_b = b.size();

  printf("%i %i\n",len_a, len_b );
  string c = a+b;
  cout << c<< endl;

  cout << swap(a,len_a) << " " << swap(b,len_b) << endl;
}