'''
WAP to find the length of the string
'''


# Python code to demonstrate string length
# using for loop

# Returns length of string
def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter


str = input('enter your string')
print(findLen(str))

'''
second method

str = input("your string is here ")
print(len(str))


# Third Method

def findLen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(str)).count(some_random_str) + 1
  
str = input("enter your string:")
print(findLen(str))
'''