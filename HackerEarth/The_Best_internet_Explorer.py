/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : This program is 'The best internet explorer' from Hacker Earth
*/
t = input()
while(t):
	t = t-1
	x = list(raw_input())
	y = len(x)
	count = 0
  for i in range(4,len(x)):
	if(x[i]=="a")or(x[i]=="e")or(x[i]=="i")or(x[i]=="o")or(x[i]=="u"):
			count1 = 0	
		else:
			count = count + 1
    e = "/"
    print("%d%s%d"%(count+1, e,y))


