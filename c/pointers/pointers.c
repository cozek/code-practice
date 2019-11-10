#include <stdio.h>

int main(int argc, char const *argv[]) {
  int x = 1, y = 2, z[10];
  int *ip;

  ip = &x;

  printf("%d\n", *ip);

  y = *ip;

  printf("%d\n",y );

  *ip = 0;

  printf("%d\n",x );

  ip = &z[0];

  printf("%d\n",z[0] );
  printf("%p\n",ip );


  return 0;
}