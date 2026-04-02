class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        candidate = -1
        n = len(nums)
        
        for i in range(n):
            if vote == 0:
                candidate = nums[i]
                vote = 1
            else:
                if nums[i] == candidate:
                    vote += 1
                else:
                    vote -= 1
        
        count = 0

        for i in range(n):
            if nums[i] == candidate:
                count += 1
        
        if count > n/2:
            return candidate
        return -1