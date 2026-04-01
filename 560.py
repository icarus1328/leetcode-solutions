class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_freq = {0:1}
        curr_sum = 0
        count = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            prev_sum = curr_sum - k

            if prev_sum in sum_freq:
                count += sum_freq[prev_sum]
            
            if curr_sum not in sum_freq:
                sum_freq[curr_sum] = 1
            else:
                sum_freq[curr_sum] += 1

        return count