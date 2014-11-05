/*
* @turlapatykaushik 
* github url : github.com/turlapatykaushik
*/

t = input()
while(t):
  t = t-1
  p = raw_input().split()
  x = int(p[0])
  y = int(p[1])
  x1 = int(p[2])
  y1 = int(p[3])
  x2 = int(p[4])
  y2 = int(p[5])
  a = x-x1
  b = x2-x
  c = y-y1
  d = y2-y
  l = [a,b,c,d]
  print min(l)
