/*
* @turlapatykaushik 
* github url : github.com/turlapatykaushik
*/

i = input()
while(i):
  i = i-1
  p = raw_input()
  q = raw_input()
  l1=list(''.join(p.split()))
  l2=list(''.join(q.split()))
  k = [x for x in l1 if x in l2]
  print len(k)
