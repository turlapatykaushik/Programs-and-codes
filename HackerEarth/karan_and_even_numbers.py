/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : This program is about the problem 'Karan and even numbers' from HackerEarth
*/

y = []
while(1):
	x = input()
	y.append(x)
	if(x==-1):
		break
for i in range(len(y)):
	if(y[i]%2==0):
		print y[i]
