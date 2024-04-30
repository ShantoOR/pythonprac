x = -5
## if x < 0:
#  raise Exception('x should not be negative.')


try:
 a=56/0
except Exception as e:   ##built-in excp
    print(e)  
    
    
try:                          ##built-in but to known catchable excp and specifying
    a = 5 / 0
except ZeroDivisionError:
    print('Only a ZeroDivisionError is handled here hehe')    


                
                
                
                
               
                        
                  
try:                                                 ## undefined but self-specified
    a = 5 / 1
    print("first case: ",a)
except:
    print('first case: some error occured.')


try:
    a = 5/0
    print("second case: ",a)
except:
    print('second case: some error occured.')
    
print("")      
    
    
   
   
    

       


    
    
try:
    a = 5/1
    print(a)  
    b = a + '10'        
    c=5/0
    print(c)              ##only one exception will be passed at a time 
        
except ZeroDivisionError as e:   
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)   
    





## else-clause
def else_clause():
    try:
        a = 5 / 1
        b=4/0
    except ZeroDivisionError as e:
        print('A ZeroDivisionError occured:', e)
    else:
        print('Everything is ok, value:',a,b)
    
    print("program running after exception")
    print("")    
    
else_clause()
    
    
    
   

try:
    a=41/0
except Exception as e:
    print("some error occured:", e)    

finally:
    print("thamaite parbe na")    
    
    
    
    
    
    
    
    
    
  
  
'''
Define your own Exceptions
You can define your own exception class that should be derived from the built-in Exception class. 
Most exceptions are defined with names that end in 'Error', similar to the naming of the standard exceptions.
Exception classes can be defined like any other class.  
'''
  
# minimal example for own exception class
class ValueTooHighError(Exception):
    pass

# or add some more information for handlers
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(a):
    if a > 1000:
        raise ValueTooHighError('Value is too high.')
    if a < 5:
        raise ValueTooLowError('Value is too low.', a) # Note that the constructor takes 2 arguments here
    return a

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, 'The value is:', e.value)
  
  
    
try:
    test_value(1425)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, 'The value is:', e.value)
      
    
    
    
    





## all exceptions: https://docs.python.org/3/library/exceptions.html

''' 

Try: This block will test the excepted error to occur
Except:  Here you can handle the error
Else: If there is no exception then this block will be executed
Finally: Finally block always gets executed either exception is generated or not

'''   