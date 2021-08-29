#WAP to uppercase HalfString

def halfUpper(string):
    halfIndex=len(string)//2

    firstHalfString=string[:halfIndex]
    secondHalfString=string[halfIndex:]
    secondHalfString=secondHalfString.upper()

    newString=firstHalfString+secondHalfString
    return newString

mystring=input("enter your string here: ")
print(halfUpper(mystring))

'''
test_str = 'WelcomeToTheLuciferWorld'
  
# printing original string
print("The original string is : " + str(test_str))
  
# computing half index
hlf_idx = len(test_str) // 2
  
# join() used to create result string 
res = ''.join([test_str[idx].upper() if idx >= hlf_idx else test_str[idx]
         for idx in range(len(test_str)) ])
          
# printing result 
print("The resultant string : " + str(res)) 
'''