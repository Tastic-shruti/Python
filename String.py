#String :Easiest 
#Length :it is the built in function that returns length of the object
print(len("I am Shruti."))
print(len("Thought of the day-Live,love,eat"))
print(len("Song-Life goes on.."))

#Concatenation
print("Shruti"+" "+"Pandey")

# Define a long_word function that accepts a string. 
# The function should return a Boolean that reflects whether the string has more than 7 characters.
# 
# EXAMPLES:
# long_word("Python")         => False
# long_word("magnificent")    => True
def long_word(str):
         return (len(str)>7)


print(long_word("python"))
print(long_word("magnificent"))

# Define a first_longer_than_second function that accepts two string arguments. 
# The function should return a True if the first string is longer than the second 
# and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")     => True
# first_longer_than_second("cat", "mouse")       => False
# first_longer_than_second("Steven", "Seagal")   => False
def first_longer_than_second(a:str,b:str):
    return (len(a)>len(b))

print(first_longer_than_second("Python","Ruby"))
print(first_longer_than_second("cat", "mouse"))
print(first_longer_than_second("Steven", "Seagal"))

#String_Indexing_with_positive_values
best_programming_language="java"
print(best_programming_language[0])
print(best_programming_language[3])
# It shows IndexError ->because we are trying to ask the value of the string position which does not exist.
#  print(best_programming_language[10])
#It shows TypeError -> because we are trying to change the defined string position value like:
#  best_programming_language[0]="B"

#TOPIC:String_indexing_with_negative_value

# The negative number value like :print(best_programming_language[-3]) represents the character 
# to extract from the end of the string

print(best_programming_language[-4])

# Questions on String indexing
# Define a same_first_and_last_letter function that accepts a string as an argument. 
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same_first_and_last_letter("runner")   => True
# same_first_and_last_letter("Runner")   => False
# same_first_and_last_letter("clock")    => False
# same_first_and_last_letter("q")        => True

def same_first_and_last_letter(str):
          return str[0]==str[-1]

print(same_first_and_last_letter("runner"))

# Define a three_number_sum function that accepts a 3-character string as an argument. 
# The function should add up the sum of the digits of the string. 
# HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.
#
# EXAMPLES:
# three_number_sum("123")   => 6
# three_number_sum("567")   => 18
# three_number_sum("444")   => 12
# three_number_sum("000")   => 0
def three_number_sum(str):
    return int(str[0])+int(str[1])+int(str[2])
print(three_number_sum("123"))

#String_Slicing_I:slicing by range
address="Visvesvaraya national institute of technology,Ambazari road,Nagpur,Maharashtra"
#including 0-> means left side and excluding right side->-1
print(address[0:-1])
print(address[0:12])
#if like this we do print(address[0:]) then it would print all the values from starting point which u told till the end letter  
print(address[0:])
print(address[:-12])

#TOPIC:String_slicing_by_steps
alphabet_letter="abcdefghijklmnopqrstuvwxyz"
print(alphabet_letter[::3])

print(alphabet_letter[::-3])

# Define a first_three_characters function that accepts a string argument.
# The function should return the first 3 characters of the string.
#
# EXAMPLES:
# first_three_characters("dynasty")   => "dyn"
# first_three_characters("empire")    => "emp"
def first_three_characters(str):
    return str[0:3]
first_three_characters("dynamic")


 #Define a last_five_characters function that accepts a string argument. 
# The function should return the last 5 characters of the string.
#
# EXAMPLES:
# last_five_characters("dynasty")   => "nasty"
# last_five_characters("empire")    => "mpire"
def last_five_characters(str):
    return str[-5:]
last_five_characters("dynasty")   
# Define a is_palindrome function that accepts a string argument. 
# The function should return True if the string is spelled 
# the same backwards as it is forwards. 
# Return False otherwise.
#
# EXAMPLES:
# is_palindrome("racecar")   => True
# is_palindrome("yummy")     => False
def is_palindrome(str):
    return str[0:]==str[::-1]
print(is_palindrome("racecar"))



#<<<<<<<<<<<<<<TOPIC :ESCAPE CHARACTERS>>>>>>>>>>
# \t
# \n
# if want to print backward slash then have to use it twice "\\"
# if want to print quote"" in the word then use it like \"\" :
print("\"Live,Love,Eat\"")
print("This will begin on a \nnew line")
print("\tOnce upon a time")
print("\"To be or not to be\",said Hamlet")
print("Let's print a backslash :\\")
file_name= r":C\news\travels" #  r -> means treat the words written as same rather than getting any escape character
print(file_name)

#<<<< TOPIC: in and not in operators for checking inclusion of a substring>>>
assignment="Holy places like vanarasi,mathura,trivandum,indore etc"
print("Holy" in assignment) 
# checking if the word or letter is included then shows True
    