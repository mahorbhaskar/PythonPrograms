# WAP to print even length words in a string

def evenLen(s):
    for i in s.split():
       if len(i)%2==0:
           print(i)
       else:
           pass

mystring=input('enter your string: ')
evenLen(mystring)