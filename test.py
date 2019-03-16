import Sort
A = [1,7,5,8,3,5,3,4,2]

print('A = ',A)

result1 = Sort.InsertionSort(A)
print('by Insertition-Sort:',result1)

result2 = Sort.MergeSort(A)
print('by Merge-Sort:',result2)

result3 = Sort.QuickSort(A,0,len(A)-1)
print('by Quick-Sort:',result3)

result4 = Sort.bucketSort(A)
print('by Bucket-Sort:',result4)


