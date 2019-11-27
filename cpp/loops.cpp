#include <iostream>
using namespace std;

bool accept()
{
  cout << "Do you want to proceed (y or n)?\n";
  char answer = 0;
  cin >> answer;

  if (answer == 'y') return true;

  return false;
}

bool accept2()
{
  cout << "Do you want to proceed (y or n)? ";

  char answer = 0;

  cin >> answer;

  switch (answer) {
    case 'y':
      return true;
    case 'n':
      return false;
    default:
      cout << "Imma assume you meant no.";
      return false;
  }
}

bool accept3()
{
  int tries = 1;
  while (tries < 4 ){
    cout << "Proceed ? [y/n]\n";
    char answer = 0;
    cin>> answer;
    switch (answer) {
      case 'y':
        return true;
      case 'n':
        return false;
      default:
        cout << "Didn't get what you said\n";
        ++tries;
    }
  }
  cout << "I will take taht as a no";
  return false;
}

int main()
{
  cout << accept3();
}