# An example of Quick sort
# Written and Edited by Isha Suri


def quick_sort(list, low, high):
    if low>=high:
        return
    pivot=partition(list, low, high)
    quick_sort(list, low, pivot-1)
    quick_sort(list, pivot+1, high)

def partition(list, low, high):
    pivot=(low+high)//2
    swap(list, pivot,high)

    i=low
    for j in range(low, high,1):
        if list[j]<=list[high]:
            swap(list,i,j)
            i=i+1
    swap(list,i, high)
    return i

def swap(list,i, j):
    temp=list[i]
    list[i]=list[j]
    list[j]=temp

list=[10,50,3,1,1000,13,4]
quick_sort(list,0, len(list)-1)
print(list)
