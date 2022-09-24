#Function :A collection of one or more statements
def _output_text():
    
 print("Welcome to programming!")
 print("Let me introduce myself...")
 print("I am Shruti pandey")
 print("I am from Chemical Department 2nd year.")
 print("Trying to be better than what I was.")
    
_output_text()
  
    #<<<Parameter and argument>>>
def p(text):
    print(text)
p("You are awesome.")
p("The code written has gone out of mind.")
    
def add(a,b,c):
     print("The sum of all three is ",a+b+c)
add(34,45,67)
#Another way to add(a=34,b=45,c=67)
add(a=100,b=23,c=34)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<Declaring Return Values for output>>>>>>>>>>>>>>>>
#Return Value:An Output from a function

def add(a,b):
 return a+b
    
result = add(34,45)
print(result)   
    
   
    
    #<<<<Default arguments :Fallback Arguments that are passed to a function if an explicit value 
    # is not provided for a parameter.

def add(a=0,b=0):
  return a+b
print(add(12,3456))

#<<<<<<<<<The_None_Type>>>>>>>>>>>
a=None
print(type(a))

def subtract(a,b):
    print(a-b)
result=subtract(34567,7890)
print(result)

#<<<<<<<<<<<<<<<<Bonus:Function Annotation>>>>>>>>>>>>>>
def word_multiplier(word:str,times:int) -> str:
    return word * times
print(word_multiplier("I will be better than what I was. ",5))