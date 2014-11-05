/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik

* problem description : pangrams
*/

x = raw_input()
y = []
for i in x:
    y.append(i)
if((y.count('a')>=1 or y.count('A')>=1) and (y.count('b')>=1 or y.count('B')>=1) and (y.count('c')>=1 or y.count('C')>=1) and (y.count('d')>=1 or y.count('D')>=1) and (y.count('e')>=1 or y.count('E')>=1) and (y.count('f')>=1 or y.count('F')>=1) and (y.count('g')>=1 or y.count('G')>=1) and (y.count('h')>=1 or y.count('H')>=1) and (y.count('i')>=1 or y.count('I')>=1) and (y.count('j')>=1 or y.count('J')>=1) and (y.count('k')>=1 or y.count('K')>=1) and (y.count('l')>=1 or y.count('L')>=1) and (y.count('m')>=1 or y.count('M')>=1) and (y.count('n')>=1 or y.count('N')>=1) and (y.count('o')>=1 or y.count('O')>=1) and (y.count('p')>=1 or y.count('P')>=1) and (y.count('q')>=1 or y.count('Q')>=1) and (y.count('r')>=1 or y.count('R')>=1) and (y.count('s')>=1 or y.count('S')>=1) and (y.count('t')>=1 or y.count('T')>=1) and (y.count('u')>=1 or y.count('U')>=1) and (y.count('v')>=1 or y.count('V')>=1) and (y.count('w')>=1 or y.count('W')>=1) and (y.count('x')>=1 or y.count('X')>=1) and (y.count('y')>=1 or y.count('Y')>=1) and (y.count('z')>=1 or y.count('Z')>=1)):
    print "pangram"
else:
    print "not pangram"
