#include <iostream>
#include <complex>
#include <vector>
using namespace std;


constexpr double square(double x)
{
  return x*x;
}

int main()
{
  double d1 {2.0};
  double d2 = 3.0;

  complex<double> z {1,2};

  vector<int> v {1,2,3,4};

  std::cout << d2 << "\n";
  std::cout << d1 << "\n";
  std::cout << z << "\n";
  for(int n : v) {
        std::cout << n << '\n';
    }

  const int dmv = 17;
  int var = 17;

  constexpr double max1 = 1.4*square(dmv);


}