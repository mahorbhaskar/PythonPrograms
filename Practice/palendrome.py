# WAP to input a number and check whether it's palendrome or not.

num = int(input("Enter a value -> "))  
temp = num  
rev = 0  
while(num > 0):  
    dig = num % 10  
    rev = rev * 10 + dig  
    num = num // 10  
if(temp == rev):  
    print("This is a palindrome number !")  
else:  
    print("This is not a palindrome number !")  