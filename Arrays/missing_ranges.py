def missing_ranges(nums,lower,upper):
    def rangeFormat(lower,upper):
        if lower==upper:
            return str(lower)
        return str(lower)+'->'+str(upper)
    res=[]
    prev=lower-1
    for i in range(len(nums)+1):
        curr=nums[i] if i<len(nums) else upper+1
        if prev+1<=curr-1:
            res.append(rangeFormat(prev+1,curr-1))
        prev=curr
    return res
print(missing_ranges([0,1,3,50,75],0,99))