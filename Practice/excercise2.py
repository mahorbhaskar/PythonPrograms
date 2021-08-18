''' Python3 program to swap elements at given positions'''

# Swap function
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# Driver function
newList = []
n=int(input("entert the size of the list : "))
for x in range(n):
    print('enter your element',x+1,':')
    listElement=int(input())
    newList.append(listElement)
print("List before swapping = ",newList)
pos1=int(input('enter element 1 position: '))
pos2=int(input('enter element 2 position: '))

print('List after swapping: ',swapPositions(newList, pos1-1, pos2-1))

