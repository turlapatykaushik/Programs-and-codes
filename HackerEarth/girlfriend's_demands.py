/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : This program is 'Girlfriend's demands' from HackerEarth
*/

x = list(raw_input())
y = input()
while(y):
	y = y-1
	a , b = map(int,raw_input().split())
	if( x[ (a-1)%len(x) ] != x[ (b-1)%len(x) ] ):
		print "No"
	else:
		print "Yes"
