/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : This program is 'Complete string' from HackerEarth
*/

from sets import Set
import string
x = string.ascii_lowercase
y = list(x)
a = set(y)
t = input()
while(t):
	t = t-1
	p = raw_input()
	q = list(p)
	b = set(p)
	if ((a.issubset(b)) ==  True):
		print "YES"
	else:
		print "NO"
