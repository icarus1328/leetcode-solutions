class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = {}
        count = 0

        for num in nums:
            need = k - num

            if need in seen and seen[need]>0:
                seen[need] -= 1
                count += 1
            else:
                if num in seen:
                    seen[num] += 1
                else:
                    seen[num] = 1

        return count