'''
WAP to Avoid Spaces in string length
'''
test_str = input('enter your string: ')

# printing original string
print("The original string is : " + str(test_str))

# isspace() checks for space
# sum checks count
res = sum(not chr.isspace() for chr in test_str)

# printing result
print("The Characters Frequency avoiding spaces : " + str(res))

'''
# Method #2 : Using sum() + len() + map() + split()

test_str = input("your string")
  
# printing original string
print("The original string is : " + str(test_str))
  
# len() finds individual word Frequency 
# sum() extracts final Frequency
res = sum(map(len, test_str.split()))
      
# printing result 
print("The Characters Frequency avoiding spaces : " + str(res)) 
'''