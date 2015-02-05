/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : Swapping program to understand the pointers
*/

#include<stdio.h>
main()
{
int a,b;
scanf("%d%d",&a,&b);
printf("Value before function call is %d %d \n",a,b);
fun1(a,b);
printf("Value after first function call is %d %d \n",a,b);
fun2(&a,&b);
printf("Value after second function call is %d %d \n",a,b);
}
fun1(i,j)
int i,j;
{
int temp;
temp = i;
i = j;
j = temp;
printf("Value during first function call is %d %d \n",i,j);
}
fun2(p,q)
int *p,*q;
{
int temp1;
temp1 = *p;
*p = *q;
*q = temp1;
printf("Value during second function call is %d %d \n",*p,*q);
}



