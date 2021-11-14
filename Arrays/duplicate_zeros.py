'''
Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

'''
def duplicate_zeros(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.pop()
            arr.insert(i + 1, 0)
            i = i + 2
        else:
            i += 1
    return arr
print(duplicate_zeros([1,0,2,3,0,4,5,0]))