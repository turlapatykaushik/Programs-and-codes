/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik

* problem description : program to generate all the prime numbers in a given range
*/

for num in range(2,100000):
    if all(num%i!=0 for i in range(2,num)):
       print num
