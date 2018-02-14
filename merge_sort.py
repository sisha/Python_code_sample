def merge_sort(list):
    if len(list)==1:
        return
    mid=len(list)//2
    left_half=list[:mid]
    right_half=list[mid:]

    merge_sort(left_half)
    merge_sort(right_half)
    i=0
    j=0
    k=0

    while i<len(left_half)and j<len(right_half):
        if left_half[i]<right_half[j]:
            list[k]=left_half[i]
            i=i+1
        else:
            list[k]=right_half[j]
            j=j+1
        k=k+1

    while i<len(left_half):
        list[k]=left_half[i]
        i=i+1
        k=k+1
    while j<len(right_half):
        list[k]=right_half[j]
        j=j+1
        k=k+1

list=[10,0,3,1000,1,14,20,2]
merge_sort(list)
print(list)
