def minsubarraylen(nums,target):
    left =0
    csum=0
    length=float('inf')
    for i,val in enumerate(nums):
        csum+=val
        while csum>=target:
            length=min(length,i+1-left)
            csum-=nums[left]
            left+=1
    if length==float('inf'):
        return 0
    else:
        return length
print(minsubarraylen([2,3,1,2,4,3],7))