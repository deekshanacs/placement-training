#include<stdio.h>
#include<string.h>
int main()
{
    char a[100];
    int length;
    printf("Enter a string you wish to calculate the length of : ");
    gets(a);
    length = strlen(a);
    printf("The length of the input string is: %d", length);
    return 0;
}
