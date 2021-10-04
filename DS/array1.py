# Program to Create an Array and perform insertion , deletion and display operations in them
from array import *

arr1 = array('i',[])
arr2 = array('i',[])
size = int(input("enter the size of the array--> "))
for i in range(size):
    val = int(input("enter the element--> "))
    arr1.insert(i,val)
    arr2.insert(i,i)
#function for inserting the element
def insert_element_inarray(array,arr2,loc):
    if loc >= len(array):
        print("index is out of bound!\n")
    else:
        val = int(input("Enter the Value"))
        array.insert(loc,val)
        n=len(arr2)
        arr2.append(n)
        print("element inserted successfully!\n")
#function for removing the element
def remove_element_inarray(array,arr2,loc):
    if loc > len(array):
        print("Your index does not locate in array! Please Try Again")
    else:
        array.pop(loc)
        arr2.pop()
        print("element remove successfully!\n")
print("################----------------##################")
#defining condition according to insertion and deletion
while True:
    print("Your Array is -> ",arr1)
    print("Array location-> ",arr2)
    choice = int(input("\npress 1 to update element on a specific location in array\npress 2 to remove the element of a specific location in a array\npress 3 to display the array\npress 4 to exit\nEnter Your Choice here -->> "))
    if choice == 1:
        loc = int(input("enter the location in the array-> "))
        insert_element_inarray(arr1,arr2,loc)
    elif choice == 2:
        loc = int(input("enter the location of the element: "))
        remove_element_inarray(arr1,arr2,loc)
    elif choice == 3:
        print(arr1)
    elif choice == 4:
        exit()
    else:
        print("wrong choice")
        