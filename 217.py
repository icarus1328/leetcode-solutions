class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = set()

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq.add(nums[i])
            else:
                return True
        
        return False