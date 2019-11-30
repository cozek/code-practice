#include <bits/stdc++.h>

using namespace std;


class dreamer{

private:
  long long num_marbles;
  long long num_colors;
public:
  dreamer (long long n, long long k){
    num_marbles = n;
    num_colors = k;
  }
  long long nChooseK(long long n, long long k){
    unsigned long long result = n;
    if (2*k>n) k = n-k;
    for (int i = 2; i <= k ; ++i){
      result *= (n-i+1);
      result /= i;
    }
    return result;
  }
  long long get_poss(){
    if (num_marbles == num_colors) {
      return 1;
    }

    return nChooseK(num_marbles-1, num_marbles - num_colors);
  }
  void printit(){
    cout << get_poss()<< endl;
  }

};


int main() {
  int num_test_cases;

  scanf("%d",&num_test_cases );

  long long num_marbles, num_colors;

  while(num_test_cases--){
    cin>>num_marbles>>num_colors;
    dreamer d = dreamer(num_marbles,num_colors);
    d.printit();
  }
}