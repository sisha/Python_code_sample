# An example of Selection sort
# Written and Edited by Isha Suri

def selection_sort(list):
    for i in range(len(list)-1):
        index=i
        for j in range(i+1, len(list)):
            if list[j]<list[index]:
                index=j
        if index is not i:
            list[i], list[index]=list[index], list[i]
    return list






list=[10,3,0,100,50,20]
print (selection_sort(list))
