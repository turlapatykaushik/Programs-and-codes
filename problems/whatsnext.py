/*
 * @turlapatykaushik
 * github url: github.com/turlapatykaushik

 * problem description : Find if three numbers are in AP or GP and print the
   next number in the sequence

def whatsnext():
    while(1):
        n = raw_input().split()
        a = int(n[0])
        b = int(n[1])
        c = int(n[2])
        if (a or b or c) == False:
            return  	
        if(b-a == c-b):
            print "AP",c + (b-a)
        else:
            print "GP",c * (b/a)
whatsnext()
    
        
    
    
        

