def house_robber_ii(nums):
    if not nums:
        return 0
    if len(nums)==1:
        return nums[0]
    dp1,dp2=0,0
    for i in nums[:-1]:
        temp=dp1
        dp1=max(i+dp2,dp1)
        dp2=temp
    dpp1, dpp2 = 0, 0
    for i in nums[1:]:
        temp = dpp1
        dpp1 = max(i + dpp2, dpp1)
        dpp2 = temp
    return max(dpp1,dp1)
print(house_robber_ii([1,2,3,1]))