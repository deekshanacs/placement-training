#include<stdio.h>
int gcd(int a,int b)
{
  if (b!=0)
    return gcd(b,a%b);
  else
    return a;
}
int main()
{
  int num1,num2:
  scanf("%d %d",&num1,&num2);
  int result = gcd(num1,num2);
  printf("GCD: %d",result);
  return 0;
}
