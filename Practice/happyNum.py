# WAP to check a number is Happy or Not
'''
Number = 3**2
3**2+ 2**2 = 13
1**2 + 3**2 = 10
1**2 + 0**2 = 1
'''

def isHappyNumber(num):    
    rem = sum = 0     
    while(num > 0):    
        rem = num%10   
        sum = sum + (rem*rem)   
        num = num//10   
    return sum   
    
# Happy number like -> 82, 13, 31, 68, 70, 97, 100 .....
     
num = int(input("enter a number ->"))   
result = num   
     
while(result != 1 and result != 4):   
    result = isHappyNumber(result)    
     
#Happy number always ends with 1    
if(result == 1):    
    print(str(num) + " is a happy number")    
#Unhappy number ends in a cycle of repeating numbers which contain 4    
elif(result == 4):    
    print(str(num) + " is not a happy number")