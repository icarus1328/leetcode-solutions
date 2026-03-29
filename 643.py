class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_winsum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i-k]
            max_winsum = max(max_winsum, window_sum)
        return (max_winsum / k)
            
        
        