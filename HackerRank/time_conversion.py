from datetime import datetime
 
def conversion(time):
    return datetime.strptime(time, '%I:%M:%S%p').strftime('%H:%M:%S')
 
 
if __name__ == '__main__':  
    input_time = raw_input()
    print conversion(input_time)
