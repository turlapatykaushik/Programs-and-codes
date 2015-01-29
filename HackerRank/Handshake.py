/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : Handshake
*/

def handshake(n):
    if(n==0):
        return 0
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    elif(n>2):
        return n * (n-1)/2
    
x = input()
while(x>0):
    x = x-1
    p = input()
    print handshake(p)
