y = []
while(1):
	x = input()
	y.append(x)
	if(x==-1):
		break
for i in range(len(y)):
	if(y[i]%2==0):
		print y[i]
