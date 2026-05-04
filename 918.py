class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        temp_sum = 0
        min_sum = float('inf')
        curr_min = 0
        total_sum = sum(nums)

        for i in range(len(nums)):
            curr_min = min(curr_min+nums[i],nums[i])
            temp_sum = max(temp_sum+nums[i],nums[i])
            max_sum = max(max_sum,temp_sum)
            min_sum = min(min_sum,curr_min)


        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)

        