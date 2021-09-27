#WAP to find the ODD frequency of character

# Using list comprehension + defaultdict()
from collections import defaultdict

# helper_function
def hlper_fnc(test_str):
	cntr = defaultdict(int)
	for ele in test_str:
		cntr[ele] += 1
	return [val for val, chr in cntr.items() if chr % 2 != 0]

# initializing string
print("enter your string: ")
test_str = input()

# printing original string
print("The original string is : " + str(test_str))

# Odd Frequency Characters
# Using list comprehension + defaultdict()
res = hlper_fnc(test_str)

# printing result
print("The Odd Frequency Characters are : " + str(res))
