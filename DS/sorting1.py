# Bubble Sort

def bubble_sort(lst):
    count = 0
    for itr_num in range(len(lst)-1,0,-1):
        for idx in range(itr_num):
            if lst[idx] > lst[idx+1]:
                temp = lst[idx]
                lst[idx] = lst[idx+1]
                lst[idx+1] = temp
        count+=1
    print("number of itteration ---->> ",count)

'''
creating an empty list 
then take the element from the user for list
'''

lst=[]
print("Enter number of Element in list")
n = int(input())

for i in range(n):
    print('enter element')
    x = int(input())
    lst.append(x)

print("List before Sorting -->> ",lst)
bubble_sort(lst)
print("List After sorting -->> ",lst)