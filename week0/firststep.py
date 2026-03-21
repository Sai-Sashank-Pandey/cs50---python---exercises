#code to ask the name
name = input("What's your name? ").strip().title()
#We could add string methods while declaring the string
'''
This is a multi line comment
'''
print("Hello",name,"!")

#Code with using END parameter
name = input("What's your name? ")
print("Hello," ,end="")
print(name)

#Formatting Strings
name=input("What's your name? ")
'''This is another way of using string methods'''
name=name.strip()
name=name.title()
'''split string function is used when you have to break a string into substrings'''
first,last=name.split()
print(f"Hello,{first}")
#f prints the string literal directly
