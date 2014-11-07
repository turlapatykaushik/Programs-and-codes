/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik

* problem description : Find the roots of a quadratic equation using python
*/

import math
a = int(raw_input("Enter a number for a"))
b = int(raw_input("Enter a number for b"))
c = int(raw_input("Enter a number for c"))
d = (b * b) - (4 * a * c)


if d < 0:
    x = (-b +  (1j * math.sqrt(-d)))/2 * a
    y = (-b -  (1j * math.sqrt(-d)))/2 * a
    print x , y
if d == 0:
    print "Roots are equal and is equal to %d " %(-b/2*a)
if d > 0:
    alpha = (-b + math.sqrt(d))/2 * a
    beta = (-b - math.sqrt(d))/2 * a
    print "Roots are distinct which are %d , %d" %(alpha,beta)
                  
