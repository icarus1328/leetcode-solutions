class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0 

        for i in nums:
            digit_count = 0
            for j in str(i):
                digit_count += 1
            if digit_count % 2 == 0:
                count += 1
        
        return count
    