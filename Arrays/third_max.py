"""
Given an integer array nums, return the third distinct maximum number in this array.
 If the third maximum does not exist, return the maximum number.
 Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""
def third_max(nums):
    maximums=set()
    for i in nums:
        maximums.add(i)
        if len(maximums)>3:
            maximums.remove(min(maximums))
    if len(maximums)==3:
        return min(maximums)
    return max(maximums)

print(third_max([1,2,3,4,5,6]))