class Solution:
    def maxArea(self, height: List[int]) -> int:
        right, left = 0, len(height)-1
        max_area = 0
        while right < left:
            area = (left - right) * min(height[right], height[left])
            max_area = max(max_area, area)
            if height[left]<height[right]:
                left -= 1
            else:
                right += 1
        return max_area