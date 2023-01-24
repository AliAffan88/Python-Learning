#!/usr/bin/env python
# coding: utf-8

# In[4]:


Text = "The quick brown fox jumps over the lazy dog"


# In[2]:


dir(str)


# # Practising all methods of string 

# In[55]:


print("-----------------------------")
print("expandtabs")
print("-----------------------------")
text = "Sentence\t with\t all\t alphabets\t of\t ABC\t"
print(text.expandtabs(2))

Text = "The quick brown fox jumps over the lazy dog.{this}".format(this = text)
print(Text)

Text = "The quick brown fox jumps over the lazy dog"


print("=============================")
print("capitalize")
print("-----------------------------")

print("#capitalize#")
print(Text.capitalize())

print("=============================")
print("casefold")
print("-----------------------------")

print("#casefold#")
print(Text.casefold())

print("=============================")
print("center")
print("-----------------------------")

print("#center#")
print(Text.center(120))

print("=============================")
print("count")
print("-----------------------------")

print("#count#")
print(Text.count(""))

print("=============================")
print("encode")
print("-----------------------------")
print("#encode#")
print(Text.encode())

print("=============================")
print("endswith")
print("-----------------------------")
print("#endswith#")
print(Text.endswith("."))

print("=============================")
print("find")
print("-----------------------------")

print("#find")
print(Text.find("f"))

print("=============================")
print("index")
print("-----------------------------")

print("#index#")
print(Text.index("u",5,25))

print("=============================")
print("replace")
print("-----------------------------")

print("=============================")
print(Text.replace(" ","."))

print("=============================")
print("format")
print("-----------------------------")
name = "Ghazwaan"
a = print(f"My name is {name}")

print('''              
        
        ''')

print("==================")
print(" BOOLEAN METHODS")
print("==================")

print("=============================")
print("islower")
print("-----------------------------")
print("#is lower#")
print(Text.islower())
print(Text.casefold().islower())

print("=============================")
print('''is alnum (Returns True if all characters in the string are alphanumeric),
        is aplha (Returns True if all characters in the string are in the alphabet), 
        is ascii Returns True if all characters in the string are ascii characters''')
print("-----------------------------")
print("#is alnum, is alpha, is ascii#")
rem_spc = Text.replace(" ","")
print(rem_spc.isalnum())
print(rem_spc.isalpha())
print(rem_spc.isascii())


print("=============================")
print('isdecimal, isdigit')
print("-----------------------------")

print("#is decimal, is digit#")
alp_num = "58a30"
num = "5830"

print(alp_num.isdecimal())
print (num.isdecimal())

print(alp_num.isdigit())
print(num.isdigit())

print(alp_num.isnumeric())
print(num.isnumeric())

print("=============================")
print('isidentifier')
print("-----------------------------")

print("#is identifier#")
print("MyFolder".isidentifier())
print("Demo002".isidentifier())
print("2bring".isidentifier()) # is not identifier if starts with number
print("my demo".isidentifier()) # is not identifier if contains space(s)


print("=============================")
print('is printable (Returns True if all characters in the string are printable)')
print("-----------------------------")
txt = "Hello!\nAre you #1?"
print(txt)
print(txt.isprintable())



print("=============================")
print('is space (Returns True if all characters in the string are whitespaces)')
print("-----------------------------")

space = "     "
print(Text.isspace())
print(space.isspace())

print("=============================")
print('is title (Returns True if the string follows the rules of a title)')
print("-----------------------------")

#The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
#Symbols and numbers are ignored.

print(Text.upper().istitle())
print(Text.casefold().istitle())
print(Text.title())
print(Text.title().istitle())


print("=============================")
print('is upper (Returns True if all characters in the string are upper case)')
print("-----------------------------")

print(Text.upper())
print(Text.upper().isupper())

print("=============================")
print('format')
print("-----------------------------")


print("End of Booleans")
print("=================")

print('''

        ''')



print("=============================")
print('join (Converts the elements of an iterable into a string)')
print("-----------------------------")
a = "."
print(a.join(Text))

print('''
''')

print("=============================")
print('ljust (Returns a left justified version of the string)')
print("-----------------------------")
a = "sentence : "
print(a.ljust(20),Text)

print("=============================")
print('rjust (Returns a right justified version of the string)')
print("-----------------------------")
a = ": sentence"
print(Text, a.rjust(5))


print('''
''')

print("=============================")
print('lower (Converts a string into lower case)')
print("-----------------------------")
caps = Text.upper()
print(caps)
print(Text.lower())

print('''
''')

print("=============================")
print('lstrip (Returns a left trim version of the string)')
print("-----------------------------")
print(Text.lstrip("T""h""e"))

print("=============================")
print('rstrip (Returns a right trim version of the string)')
print("-----------------------------")
print(Text.rstrip("f""o""x"))
print('''
''')

print("=============================")
print('''maketrans (Returns a translation table to be used in translations)
        translate (Returns a translated string)''')
print("-----------------------------")
mt = Text.maketrans("The","  a")
print(Text.translate(mt))
print("                          ")
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z)) 
print(txt.translate(txt.maketrans(x, y, z))) #to practice more

print('''
''')

print("=============================")
print('''partition (The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
The first element contains the part before the specified string.
The second element contains the specified string.
The third element contains the part after the string.)''')
print("-----------------------------")
print(Text.partition("fox"))


# In[ ]:





# In[ ]:




