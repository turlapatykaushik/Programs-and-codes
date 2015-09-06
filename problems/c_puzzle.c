#include<stdio.h>
#define concat(a,b) a##b

int main()
{
	printf("%d\n",concat(36,12));
	return 0;
}
