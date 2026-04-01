class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n - 1
        right = m+n-1
        left = m - 1
        while i >= 0:
            if left >= 0:
                if nums2[i] > nums1[left]:
                    nums1[right] = nums2[i]
                    i -= 1
                    right -= 1
                else:
                    nums1[right] = nums1[left]
                    left -= 1
                    right -= 1
            else:
                nums1[right] = nums2[i]
                right -= 1
                i -= 1