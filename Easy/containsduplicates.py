def containsduplicates(nums):
    d=set()
    for i in nums:
        if i not in d:
            d.add(i)
        else:
            return True
    return False
print(containsduplicates([1,2,3,4]))
