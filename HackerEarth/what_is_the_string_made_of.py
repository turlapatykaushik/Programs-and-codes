/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : This program is about the problem 'what is the string made of' from HackerEarth
*/

dict = { '1' : 2, '2' : 5, '3' : 5, '4' :4, '5' : 5, '6' : 6, '7' : 3, '8' : 7, '9': 6, '0':6}
x = list(raw_input())
sum = 0
for i in range(len(x)):
	sum = sum + dict[x[i]]
print sum

