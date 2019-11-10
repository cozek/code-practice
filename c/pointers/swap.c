#include <stdio.h>
void swap(int *pa, int *pb);


void swap(int *pa, int *pb)
{
  int temp;

  temp = *pa;
  *pa = *pb;
  *pb = temp;
}

int main(int argc, char const *argv[]) {
   int a = 4, b = 3;

   swap(&a, &b);
   printf("a=%d , b=%d\n",a,b );

  return 0;
}