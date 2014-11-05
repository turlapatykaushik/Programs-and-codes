/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik

* problem description : lonely integer
*/

y = input()
a = [int(x) for x in raw_input().split()]
for i in a:
    if(a.count(i)== 1):
        print i
