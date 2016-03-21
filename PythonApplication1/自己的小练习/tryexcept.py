
import sys

s=input("input your age:")  

try:  
    i=int(s)  
except Exception as err:  
    print('ERROR',err)  
finally:  
    print("Goodbye!") 

