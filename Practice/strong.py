'''
A Strong number is a special number whose sum of the all digit factorial should be equal to the number itself.
number is --> 145
1! = 1, 4! = 24, and 5! = 120
1 + 24 + 120 = 145
'''
sum = 0  
num = int(input("Enter a number:")) 
temp=num 
while(num):
    i=1  
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i   
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print(temp," is a strong number")  
else:  
    print(temp," is not a strong number")  