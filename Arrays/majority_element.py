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

'''
approach 2:
-----------

nums.sort()
return nums[len(nums)//2]

-------
approach 3:
------

count=Counter(nums)
return sort(count.keys(),key=count.get)
'''
print(majority([3,2,3,2,2,2]))