/*
 * @turlapatykaushik
 * github url : github.com/turlapatykaushik

 * problem description : 'AddReverse' problem from codechef
*/

t = input()
while(t):
    t = t-1
    n = raw_input().split()
    a = n[0][-1::-1]
    b = n[1][-1::-1]
    c = str(int(a)+int(b))[-1::-1]
    print int(c)
    
