import socket

name = raw_input("Enter website here: ") 
try:
    host = socket.gethostbyname(name)
    print "Your Domain IP address is:" , host
except socket.gaierror, err:  
    print "Cannot resolve hostname: ", name, err
    
    
    
    
    

