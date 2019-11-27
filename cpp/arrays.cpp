#include <iostream>
using namespace std;

void prin(int d[], int size)
{
  for (auto i =0; i<size; i++)
    cout<<d[i];
}

void copy_fct()
{
  int v1[10]{0,1,2,3,4,5,6,7,8,9};

  int v2[10];

  for (auto i=0;i!=10;i++)
  {
    v2[i] = v1[i];
  }

  for (auto &n: v2)
  {
    cout << n<< " ";
  }
  // prin(v2,10);
}


int main()
{
  /*size of an array must be a constant expressino*/
  int size = 6;
  char v[size]; //array of 6 characters

  char* p; //pointer to a character;
  p = &v[3]; //points to v's 4th character

  char x = *p; // *p is the object p points to
  copy_fct();
}