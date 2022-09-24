# Method: A function that acts upon a specific object
# <<<<<<<Assignment:The find and count Methods
# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLES:
# vowel_count("estate")        => 3
# vowel_count("helicopter")    => 4
# vowel_count("ssh")           => 0
#def vowel_count(str):
   # return 

# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string
#
# EXAMPLES:
# find_my_letter("dangerous", "a")    => 1
# find_my_letter("bazooka", "z")      => 2
# find_my_letter("lollipop", "z")     => -1
def find_my_letter(a:str,b:str):
    return a.find(b)
print(find_my_letter("dangerous","a"))
print(find_my_letter("lollipop","z"))

#<<<<TOPIC:Capitalize,Lower,title,upper
# capitalize here means just first word of the sentence is capital
# title here means all the word in a sentence has first letter capital
# lower here means all in lowercase 
# swapcase here means exchange the case means lower in upper and upper in lower

intro="I am Shruti pandey."
print(intro.capitalize())
print(intro.lower())
print(intro.title())
print("sHRUTI".swapcase())

#<<<<BOOLEAN METHOD>>>>
print("u are always being judged by someone".islower())
print("LIFE GOES ON".isupper())
print("I will make my parents proud".istitle())
print("area".isalnum())
print(" ".isspace())
print("arre ".isspace())

# <<<<<<<<<<<<<<<<<<< Istrip,rstrip and strip methods>>>>>>>
empty_space="    content    "
print(empty_space.rstrip())
print(len(empty_space.rstrip()))
print(empty_space.lstrip())
print(len(empty_space.lstrip()))
print(empty_space.strip())
print(len(empty_space.strip()))

website="www.python.org"
phone_number="555 512 3456" 
print(phone_number.replace(" ","-"))

# Define a fancy_cleanup function that accepts a single string argument
# The function should clean up the whitespace on both sides of the
# argument. It should also replace every occurrence of the letter "g" with the
# letter "z" and every occurence of a space with an exclamation point (!).
#
# fancy_cleanup("       geronimo crikey  ")   => "zeronimo!crikey"
# fancy_cleanup("       nonsense  ")          => "nonsense"
# fancy_cleanup("grade")                      => "zrade"

def fancy_cleanup(str):
    return  str.strip().replace(" ","!").replace("g","z")


print(fancy_cleanup("    Life goes on   "))

#<<<<<<<<<<TOPIC: The format method
# name,adjective,noun
mad_lib="{} a time, story starts like {}"
print(mad_lib.format("Once","this"))
family_member="{},{},mithi,saloni,{},krishna.....{}"
print(family_member.format("papa","mummy","sneha","miss u all leaving myself"))
mad_lib="{name} laughed at the {adjective} {noun}"
print(mad_lib.format(name="Jennifer",adjective="green",noun="alien"))
name=input("Enter a name : ")
adjective=input("Enter an adjective for the name : ")
noun=input("Enter the noun : ")
print(mad_lib.format(name =name,adjective =adjective,noun =noun))

#<<<<<<<formatted string literals>>>>>>>>
name1="Mummy"
name2="Papa"
name3="everyone"
family_mem=f"{name1},{name2} and {name3} miss u all"
print(family_mem)
print(f"2 + 2 is {2+2}")