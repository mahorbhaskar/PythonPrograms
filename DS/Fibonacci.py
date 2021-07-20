'''
a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
The simplest is the series 1, 1, 2, 3, 5, 8, etc.
'''
def fibo(n):
    if (n==1):
        return 0
    if(n==2):
        return 1
    return (fibo(n-1)+fibo(n-2))

n=int(input("Enter No. of Terms: "))
for i in range(1,n+1):
    print(fibo(i))