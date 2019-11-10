#include <stdio.h>

int main(int argc, char const *argv[]) {
  int x = 1, y , z[10];
  int *ip;

  ip = &x;


  printf("Value at pointer: %d\n",*ip );

  y = *ip + 2; //take whatever ip points to and add 2

  printf("Value of y: %d\n",y );

  *ip += 1; // increments whatever ip points to.

  ++*ip; //same as above

  (*ip)++ ;//same as above

  printf("%d\n",x );

  //since pointers are variables, they can be used without dereferencing
  int *iq;

  iq = ip; // iq points to whatever ip points to

  printf("%d\n", *iq);

  return 0;
}