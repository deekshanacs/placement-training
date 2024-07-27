#include<stdio.h>
void main()
{
    int n,i,j,temp,arr[40];
    printf("Enter how many values you want to read : ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("Enter the value of a[%d] : ",i);
        scanf("%d",arr[i]);
    }
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(arr[j]>arr[j+i])
            {
                temp=arr[j];
                arr[j]=arr[j+i];
                arr[j+1]=temp;
            }
        }
    }
    printf("Array sorted in ascending order = ");
    for(i=0;i<n;i++)
    {
        printf("%d",arr[i]);
    }
    printf("\n");
}
