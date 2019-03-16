def InsertionSort(list): 
    length = len(list)
    for i in range(1,length):
        key = list[i]
        j = i-1
        while j>=0 and list[j]>key:
            list[j+1] = list[j]
            j-=1
        list[j+1] = key
    return list



def MergeSort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = MergeSort(list[:mid])
    right = MergeSort(list[mid:])
    return Merge(left,right)

def Merge(left,right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i += 1
        
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result



def QuickSort(list,l,r):
    if(l>=r):
        return list
    p = partition(list,l,r)
    QuickSort(list,l,p-1)
    QuickSort(list,p+1,r)
    return list

def partition(list,l,r):
    x = list[r]
    i = l-1
    for j in range(l,r):
        if list[j]<= x:
            i += 1
            list[i],list[j] = list[j],list[i]
    list[i+1],list[r] = list[r],list[i+1]
    return i+1



def bucketSort(list):
    buckets = [0]*(max(list)-min(list)+1)
    for i in range(len(list)):
        buckets[list[i]-min(list)] +=1
    b = []
    for i in range(len(buckets)):
        if(buckets[i])!= 0:
            b += [i+min(list)] * buckets[i]
    return b   







