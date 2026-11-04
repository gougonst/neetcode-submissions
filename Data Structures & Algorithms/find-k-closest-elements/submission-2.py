class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            m = l + (r - l) // 2

            if abs(arr[m] - x) > abs(arr[m + k] - x):
                l = m + 1
            else:
                r = m
        return arr[l:l + k]
        