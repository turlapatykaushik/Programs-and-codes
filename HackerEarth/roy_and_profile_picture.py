/*
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description : This program is 'roy and profile picture from HackerEarth
*/

l = input()
t = input()
while(t):
    t = t-1
    w,h = map(int, raw_input().split())
    if( w < l)or ( h < l):
        print "UPLOAD ANOTHER"
    else:
        if(w==h):
            print "ACCEPTED"
        else:
            print "CROP IT"
