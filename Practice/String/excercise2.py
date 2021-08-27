'''
WAP to remove i’th character from string in Python
'''
# Python code to demonstrate
# method to remove i'th character
# Naive Method

# Initializing String

test_str = input('enter you string: ')

# Printing original string
print("The original string is : " + test_str)

# Removing char at pos 3
# using loop
new_str = ""
n=int(input('enter the position of character you want to remove: '))
for i in range(len(test_str)):
    if i != n:
        new_str = new_str + test_str[i]

# Printing string after removal
print("The string after removal of i'th character : " + new_str)