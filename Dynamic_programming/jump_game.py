def jump_game(nums):
    goal=len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if nums[i]+i>=goal:
            goal=i
    return True if goal==0 else False
print(jump_game([2,3,1,1,4]))
print(jump_game([3,2,1,0,4]))