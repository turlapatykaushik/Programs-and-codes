'''
* @turlapatykaushik
* github url : github.com/turlapatykaushik
* problem description :  Python Program to reverse a number and check if its a palindrome or not
'''

x = raw_input("Enter a string to check if its a palindrome or not")
y = x[::-1]
if(x==y):
    print "It is a palindrome"
else:
    print "It is not a palindrome"
    
