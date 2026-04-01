class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        curr_max = 1
        curr_min = 1
        
        for i in range(len(nums)):
            temp_min = nums[i]*curr_min
            curr_min = min(nums[i], temp_min, nums[i]*curr_max)
            curr_max = max(nums[i], temp_min, nums[i]*curr_max)
            

            max_prod = max(max_prod, curr_max)
        
        return max_prod