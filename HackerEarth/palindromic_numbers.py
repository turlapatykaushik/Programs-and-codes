/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : This problem is 'Palindromic Numbers' from HackerRank
*/

def pal(n):
	x = map(int, str(n))
	y = x[::-1]
	if(x==y):
		return True
	else:
		return False

m = input()
while(m):
	count = 0
	m = m-1
	p,q = map(int, raw_input().split())
	for i in range(p,q+1):
		if(pal(i)):
			count = count + 1
		else:
			count2 = 0
	print count
