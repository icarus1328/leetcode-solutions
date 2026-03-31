class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        temp_sum = 0
        
        for right in range(len(nums)):
            temp_sum = max(nums[right], temp_sum+nums[right])
            
            max_sum = max(max_sum, temp_sum)
            
        
        return max_sum