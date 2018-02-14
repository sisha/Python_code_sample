# An example of bubble sort
# Written and modified by Isha Suri


def bubble_sort(list):
    for i in range (len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j], list[j+1]=list[j+1], list[j]
    return list


list=[2,1,1000,4,0,1000,90]
print (bubble_sort(list))
