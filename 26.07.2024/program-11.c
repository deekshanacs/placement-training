#include<stdio.h>
int main()
{
  float x,a,c,d,b,p;
  printf("Number of copies sold");
  scanf("%f",&x);
  printf("Cost of each company");
  scanf("%f",&a);
  printf("Cost spemt by the gaengy on newspaper : ")
  scanf("%f",&b);
  c=x*a;
  d=c-b*x;
  p=d-100;
  printf("The profit obtained is : Rs.%.6f",p);
  return 0;
}
