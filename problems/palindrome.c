/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description :  C Program to reverse a number and check if its a palindrome or not
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
	int num,temp,rev=0,rem;
	printf("The number to check if it is palindrome or not");
	scanf("%d",&num);
	temp = num;
	while(num!=0)
	{
		rem = num % 10;
		rev = (rev*10) + rem;
		num = num / 10;
	}
	printf("The reverse of the number %d is %d\n",temp,rev);
	if(rev==temp)
	{
		printf("It is a palindrome");
	}
	else
	{
		printf("It is not a palindrome");
	}
	return 0;
}
