# initializing strings
print('enter a string: ')
test_str1 = input()
print('enter string that you want to search: ')
test_str2 = input()
  
# printing original string
print("The original string is : " + test_str1)
  
# Test if string is subset of another
# Using all()
res = all(ele in test_str1 for ele in test_str2)
  
# printing result 
print("Does string contains all the characters of other list? : " + str(res)) 