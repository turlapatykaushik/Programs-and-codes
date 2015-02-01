def fac(n):
    if(n==0):
	return 1
    elif(n==1):
	return 1
    else:
	return n * fac(n-1)
t = input()
while(t):
	t = t-1
	x = input()
	p = fac(x)
	print p 
