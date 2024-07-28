#include<stdio.h>
#include<math.h>
int main()
{
    int x1,x2,x3,y1,y2,y3;
    printf("x y coordinates of vertex A : ");
    scanf("%d %d",&x1,&y1);
    printf("x y corodinates of vertex B : ");
    scanf("%d %d",&x2,&y2);
    printf("x y corodinates of vertex C : ");
    scanf("%d %d",&x3,&y3);
    int ab,bc,ac;
    ab=(pow(x2,2)-pow(x1,2)+pow(y2,2)-pow(y1-2));
    bc=(pow(x3,2)-pow(x2,2)+pow(y3,2)-pow(y2,2));
    ac=(pow(x1,2)-pow(x3,2)+pow(y1,2)-pow(y3,2));
    printf("Length Ab : %d\n",ab);
    printf("Length BC: %d\n",bc);
    printf("Length Ac: %d\n",ac);
}
