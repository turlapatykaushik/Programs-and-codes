/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : This problem is 'Crazy Kangaroo' from HackerEarth
*/

t = input()
while(t):
    count = 0
    t = t-1
    x = raw_input().split()
    a = int(x[0])
    b = int(x[1])
    m = int(x[2])
    print (b/m - (a+m-1)/m +1)
