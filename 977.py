class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n
        left, right = 0 , n - 1
        pos = n - 1

        while right >= left:
            if abs(nums[left]) > abs(nums[right]):
                temp = nums[left] ** 2
                arr[pos] = temp
                left += 1
            else:
                temp = nums[right] ** 2
                arr[pos] = temp
                right -= 1
            pos -= 1
        
        return arr