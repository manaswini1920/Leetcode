"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
def square_of_sorted_array(nums):
    for idx in range(len(nums)):
        nums[idx]=nums[idx] **2
    return sorted(nums)

"""
approach 2:
final=[None for _ in nums]
left =0
right=len(nums)-1
for i in range(len(nums)-1,-1,-1):
    if abs(nums[left])>abs(nums[right]):
        final[i]=nums[left]**2
        left+=1
    else:
        final[i]=nums[right]**2
        right-=1
return final
"""
print(square_of_sorted_array([-4,-1,0,3,10]))
