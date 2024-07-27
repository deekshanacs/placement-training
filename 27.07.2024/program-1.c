#include<stdio.h>
struct Phone
{
    int emino;
    char name[30];
    char colour[30];
    int modelno;
};
int main()
{
    struct Phone p;
    printf("Enter the emino : ");
    scanf("%d",&p.emino);
    printf("Enter the name : ");
    scanf("%s",p.name);
    printf("Enter the colour : ");
    scanf("%s",p.colour);
    printf("enter the model.no : ");
    scanf("%d",&p.modelno);
    printf("The Details are\n");
    printf("Emi number : %d\n",p.emino);
    printf("Name : %s\n",p.name);
    printf("Colour : %s\n",p.colour);
    printf("Model No :%d\n",p.modelno);
}
