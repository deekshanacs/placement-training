#include<stdio.h>
int main()
{
    int a,b[50],cnt=0;
    printf("Enter how many values do you want to read : ");
    scanf("%d",&a);
    printf("Enter %d values : ",a);
    for(int i=0;i<a;i++)
    {
        scanf("%d",b[i]);
        if(b[i]<0)
        {
            cnt++;
        }
    }
    printf("The number of positive numbers : %d\n",a-cnt);
    printf("The number of negative numbers : %d\n",cnt);
}
