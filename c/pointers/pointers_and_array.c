#include <stdio.h>
int strlenth(char *s);


int main(int argc, char const *argv[]) {
  int a[10];

  // a[0] = 1;

  int *pa;

  pa = &a[0]; // pa contains the address of array a

  pa = a; //same as above

  //p[i] is the same as *(p+i)

  printf("%d\n",*(pa+0) );

  printf("%d\n", strlenth("hello!"));

  return 0;
}

int strlenth(char *s)
{
  int n;

  for(n=0; *s!='\0'; s++) // its legal to pointer++
  {
    n++;
  }

  return n;
}