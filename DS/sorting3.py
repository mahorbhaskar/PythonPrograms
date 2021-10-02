# Insertion Sort 

def insertion_sort(list1):
    indexing_length = range(1,len(list1))
    for i in indexing_length:
        value_to_sort = list1[i]

        while list1[i-1] > value_to_sort and i>0:
            list1[i], list1[i-1]= list1[i-1], list1[i]
            i = i-1

    return list1

print(insertion_sort([33,22,11,21,10,13,35,8,25]))