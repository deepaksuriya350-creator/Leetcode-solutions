class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if len(nums) < 3 :
            return max(nums)
        n = len(nums)
        dp = [0] * n
        dp[1] , dp[2] = nums[1] , max(nums[1] , nums[2])
        for i in range(3 , n) :
            dp[i] = max(dp[i-1] , dp[i-2]+nums[i])
        dp[0] , dp[1] = nums[0] , max(nums[0] , nums[1])
        for i in range(2 , n-1) :
            dp[i] = max(dp[i-1] , dp[i-2]+nums[i])
        return max(dp[-1] , dp[-2])