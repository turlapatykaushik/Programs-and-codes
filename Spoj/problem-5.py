/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
*/
 
from fractions import gcd
from functools import reduce
def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    return a*b//gcd(a,b)
k = reduce(lcm, range(1,20+1))
print k
