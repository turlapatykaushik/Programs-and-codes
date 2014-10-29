/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
*/
#include<stdio.h>
#include<stdlib.h>
int main()
{
	int x,y,a,b,lcm,gcd,rem;
	printf("Enter the two numbers whose gcd and lcm is to be found");
	scanf("%d%d",&a,&b);
	x=a;
	y=b;
	if(a==0 && b==0)
	{
		printf("Cannot find GCD");
	}
	else
	{
		while(x!=0)
		{
			rem = y % x;
			y = x;
			x = rem;
		}
		gcd = y;
		lcm = (a*b)/gcd;
		printf("The GCD and LCM of %d and %d is %d and %d",a,b,gcd,lcm);
	}
	return 0;
}
	
