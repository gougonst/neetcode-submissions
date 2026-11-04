class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            nums1[m + n - 1 - i] = nums1[m - 1 - i]

        l, r = n, 0
        i = 0
        while l < m + n and r < n:
            if nums1[l] <= nums2[r]:
                nums1[i] = nums1[l]
                l += 1
            else:
                nums1[i] = nums2[r]
                r += 1
            i += 1

        while l < m + n:
            nums1[i] = nums1[l]
            l += 1
            i += 1
        while r < n:
            nums1[i] = nums2[r]
            r += 1
            i += 1