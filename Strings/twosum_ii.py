"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
"""
def twosumii(nums,target):
    d=dict()
    for i,j in enumerate(nums):
        compliment =target-j
        if compliment not in d:
            d[j]=i
        else:
            return [i,d[compliment]]

print(twosumii([2,7,11,15], 9)) #index 0,1