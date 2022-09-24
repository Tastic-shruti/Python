#TOPIC:The Boolean Type
handsome="False"
admin="False"
print(2<4)
result=4>=5
print("boris"=="Boris")
print(result)
print("Boris"!="boris")
print(True!=False)      

#<<TOPIC:If statement>>
if (5>3):
    print("Hurray!,it will be printed....")
    print("This is printed becoz the statement was true.")
if(4<=8):
    print("Hope this is not false,so it has to be printed.")
if(5==5):
    print("Shruti -the name will be printed.") 
if True:
    print("Always true,always print.")    
if False:
    print("Never true,not to print.")
    
# The bool function
# if 3 is written it means truthy be cause leaving 0 because it is a falsy value.
if 3:
    print("Hello!")
if 7:
     print("Goodbye")  
if 0:
    print("Life Goes On")
if 1:
    print("Pasoori") 
if "":
    print("This will not print.")  
print(bool(1))          
print(bool(0))

# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#
# even_or_odd(2)    => "even"
# even_or_odd(0)    => "even"
# even_or_odd(13)   => "odd"
# even_or_odd(9)    => "odd"
def even_or_odd(int):
    if int%2==0: 
        return "even"
            
        return "odd"
    print(even_or_odd(77))
# Define a truthy_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value _____ is ______" 
# where the first space is the argument and the second space 
# is either 'truthy' or 'falsy'. See the sample invocations below.
# 
# truthy_or_falsy(0)        => "The value 0 is falsy"
# truthy_or_falsy(5)        => "The value 5 is truthy"
# truthy_or_falsy("Hello")  => "The value Hello is truthy"
# truthy_or_falsy("")       => "The value  is falsy"

    def truthy_or_falsy(value):
        if bool(value):
            return f"The value {value} is Truthy."
            return f"The value {value} is Falsy."
        print(truthy_or_falsy(56)) 
        print(truthy_or_falsy(0)) 
    
    #<<<<<<<<<<<<<<TOPIC:else statement>>>>>
value=int(input("Enter any random no. : "))
if value > 1000000:
    print("I like that you are thinking big!!")
else:
     print("It is OK number I guess....")   
  #<<<<<< TOPIC: elif statement >>>>>>
def positive_or_negative(number) :
     if number >0:
        return "Positive!"
     elif number <0:
        return "Negative!" 
     else :
        return "Neither!It's zero." 
def calculator(operation,a,b):
    if operation=="add":
        return a+b
    elif  operation=="subtract":
        return a-b          
    elif operation=="multiply":
        return a/b
    else:
        return "I don't know what you want me to do!"
    
print(calculator("add",3,4))   
print(calculator("subtract",3,4))

#<<<<<<< Topic Assignment : if,else,elif >>>>>>>
# Declare a negative_energy function that accepts a numeric argument and returns its absolute value. 
# The absolute value is the number's distance from zero.
# 
# negative_energy(5)    => 5
# negative_energy(10)   => 10
# negative_energy(-5)   => 5
# negative_energy(-8)   => 8
# negative_energy(0)    => 0

def negative_energy(number:int):
    
    
    if number > 0 :
     return f"The number is {number}"
    elif number < 0:
        return -1*number 
    else:    
     return number
print(input(negative_energy(-56)))

#<<<<<<TOPIC: Conditional Expression(Ternary operator equivlent) >>>>>>
pin_code="273014"
 #check
if len(pin_code)==5:
     check="valid"
else:
     check="invalid"
print(check)     
# ternary method
option="Valid" if len(pin_code)=="273014" else "Invalid"

#elif statement
def positive_or_negative(Number:int):
 if Number>0:
  return "Positive" 
 elif Number<0:
    return "Negative!" 
 else:
    return "Neither!It's zero."
print(positive_or_negative(34))
print(positive_or_negative(-78))
print(positive_or_negative(0))

def calculator(operation,a,b):
    if operation=="add":
        return a+b
    elif operation=="subtract":
        return a-b
    elif operation=="multiply":
        return a*b
    elif operation=="division":
        return a/b
    else:
        return "I don't know what u want me to do!"
print(calculator("multiply",4567,78))

#Declaring multiple conditions with the "&" keyword

if 5<7 and "rain"=="rain" :
    print("Both of those conditions evaluate to True.") 
if 5>7 and "rain"=="rain":
    print("This will not print because at least one of the two conditions is false.")
if 5>7 and "rain"=="drop":
    print("This will not print because at least one of the two conditions is false.") 
    
 # <<<<<<<<<<<<<<<<"or" keyword >>>>>>>>>>>>>>>>
 
if 5>8 or 7<11:
     print("At least one of the conditions is True!")
if "cat"=="cat" or "dog"=="donkey":
    print("At least one of the conditions is True!")
if "apple"=="banana" or "orange"=="pear":
    print("Will this print?Nope!")   
    
# Using the not keyword to negate an expression

print(not True)     
print(not False)

if "H" in "Hello":
    print("That character exists in the string!!")
if "Z" not in "Hello":
    print("That character does not exist in the string!")
    
value=10
if value>100:
    print("This will not print!")
if value<100:
    print("This will print!")    
            
# Define a divisible_by_three_and_four function that accepts a number as its argument. 
# It should return True if the number is evenly divisible by both 3 and 4 . 
# It should return False otherwise.
#
# divisible_by_three_and_four(3)   => False
# divisible_by_three_and_four(4)   => False
# divisible_by_three_and_four(12)  => True
# divisible_by_three_and_four(18)  => False
# divisible_by_three_and_four(24)  => True




#<<<<<<<Using the while loop to iterate while a condition is true>>>>>>>
            
    
         
 
              