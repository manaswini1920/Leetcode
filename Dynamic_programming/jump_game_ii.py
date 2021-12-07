def jump_game_ii(nums):
    far=end=jump=0
    for i in range(len(nums)-1):
        far=max(far,nums[i]+i)
        if i==end:
            jump+=1
            end=far
    return jump
print(jump_game_ii([2,3,1,1,4]))