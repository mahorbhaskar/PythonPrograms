#WAP to capitalize the first and last character of each word in a string

def word_cap(str):
    # lamda function for capitalizing the
    # first and last letter of words in
    # the string
    return ' '.join(map(lambda str: str[:-1] + str[-1].upper(),
                        str.title().split()))


# Driver's code
mystring = input('enter your string here: ')
print("String before:", mystring)
print("String after:", word_cap(mystring))

