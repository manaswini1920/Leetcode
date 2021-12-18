def majority(nums):
    d=dict()
    n=len(nums)//2
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i,j in d.items():
        if j>n:
            return i
print(majority([3,2,3,2,2,2]))