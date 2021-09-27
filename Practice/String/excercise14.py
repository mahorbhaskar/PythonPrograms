# WAP to Least Frequent character in string

print("enter your string:")
test_str = input()

# printing original string
print ("The original string is : " + test_str)


# Least Frequent Character in String
all_freq = {}
for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1
res = min(all_freq, key = all_freq.get)

# printing result
print ("The minimum of all characters in GeeksforGeeks is : " + str(res))
