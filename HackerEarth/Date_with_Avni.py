/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : This program is about the problem 'Date with Avni' from HackerEarth
*/

t = input()
while(t):
	count = 0
	t = t-1
	x = list(raw_input())
	for i in range(len(x)-1):
		if(x[i]==x[i+1]):
			print "SLAP"
			break
		else:
			count = count + 1
			if(count == len(x)-1):
				print "KISS"
			else:
				count3 = 1
			
			
		
