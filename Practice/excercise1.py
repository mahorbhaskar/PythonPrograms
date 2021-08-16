'''Python program to find the
  maximum of two numbers'''


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


# Driver code
a = int(input('enter first number: '))
b = int(input('enter second number: '))
print('The Maximum number is: ',maximum(a, b))