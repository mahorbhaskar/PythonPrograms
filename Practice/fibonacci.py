# WAP to create a fabonacci series
start = int(input("starting term "))
term = int(input("enter the ending term "))
mid = 1
nextTerm = start
count = 0
lst = []
while count < term:
    lst.append(nextTerm)
    start = mid
    mid = nextTerm
    nextTerm= start + mid
    count+=1
print("Your Fibonnaci Seiries is -> ")
print(lst)