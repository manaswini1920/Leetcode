'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
 To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
'''
def merge_sorted_arrays(nums1,nums2):
    i = 0
    j = 0
    while i < len(nums1):
        if nums1[i] < nums2[j]:
            nums1.insert(i + 1, nums2[j])
            i += 1
            j += 1
        elif nums1[i] >= nums2[j]:
            nums1.insert(i, nums2[j])
            j += 1
            i += 1
    return nums1
print(merge_sorted_arrays([1,2,3,0,0,0],[2,5,6]))