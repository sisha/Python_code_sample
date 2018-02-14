# An example of Insertion sort
# Written and Edited by Isha Suri

def insertion_sort(list):
    for i in range(1, len(list)):
        j=i
        while j>0 and list[j-1]>list[j]:
            list[j-1], list[j]=list[j], list[j-1]
            j=j-1
    return list




list=[100,0,-1,50,4,10]
print(insertion_sort(list))
