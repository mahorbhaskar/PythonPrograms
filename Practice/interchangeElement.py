# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


# Driver code
newList = []
n=int(input("entert the size of the list : "))
for x in range(n):
    print('enter your element',x+1,':')
    listElement=int(input())
    newList.append(listElement)
print("List before interchange first and last element = ",newList)
print("List after interchange first and last element = ",swapList(newList))