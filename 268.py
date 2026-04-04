class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp_sum = 0
        act_sum = sum(nums)

        for i in range(len(nums)+1):
            exp_sum += i
        
        return exp_sum - act_sum