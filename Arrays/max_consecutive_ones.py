"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Input: nums = [1,0,1,1,0,1]
Output: 2
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
"""
def max_consecutive_ones(nums):
    i=0
    count=0
    max_count=0
    while i<len(nums):
        if nums[i]==1:
            count+=1
        else:
            max_count=max(count,max_count)
            count=0
        i+=1
    max_count=max(count,max_count)
    return max_count
print(max_consecutive_ones([1,1,0,1,1,1]))
