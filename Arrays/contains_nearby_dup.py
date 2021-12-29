def contains_nearby_dup(nums,k):
    visited=set()
    for i in range(len(nums)):
        if nums[i] in visited:
            return True
        visited.add(nums[i])
        if len(visited)>k:
            visited.remove(nums[i-k])
    return False
print(contains_nearby_dup([1,2,3,1],3))