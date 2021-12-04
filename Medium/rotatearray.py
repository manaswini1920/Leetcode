class Solution: #O(n),O(1)
    def reverse(self,nums,left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left,right=left+1,right-1
    def rotate(self,nums,k):
        k=k%len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
        return nums
s=Solution()
print(s.rotate([1,2,3,4,5,6,7],3))