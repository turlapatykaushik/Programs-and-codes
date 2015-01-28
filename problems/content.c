/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik

* problem description : This program copies content from one file to the other
*/

#include<stdio.h>
#include<stdlib.h>
int main()
{
	char ch;
	FILE *fp_in,*fp_out;
	fp_in=fopen("input.txt","r");
	fp_out=fopen("output.txt","w");
	while(!feof(fp_in))
	{
		ch=fgetc(fp_in);
		if(feof(fp_in))
		{
			break;
		}
		fputc(ch,fp_out);	
	}
	fclose(fp_in);
	fclose(fp_out);
	return 0;
}
