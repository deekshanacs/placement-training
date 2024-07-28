#include<stdio.h>
int main()
{
    char mar;
    char gen;
    int age;
    printf("Enter martial Status (M/U): ");
    scanf("%c",&mar);
    printf("Enter gender (M/F) :\n");
    scanf("%c",&gen);
    printf("Enter the age : ");
    scanf("%d",&age);
    if(mar=='M')
    {
        mar='m';
    }
    else if(mar=='U')
    {
        mar='u';
    }
    else if(gen=='M')
    {
        gen='m';
    }
    else if(gen=='F')
    {
        gen='f';
    }
    if(mar=='m'||(gen=='m'&&age>30)||(gen=='f'&&age>25))
    {
        printf("Driver is insured\n");
    }
    else
    {
        printf("Driver is not insured\n");
    }
}
