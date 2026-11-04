class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l: int, r: int) -> int:
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]

            if p == k: return nums[p]
            elif p < k: return quickSelect(p + 1, r)
            else: return quickSelect(l, p - 1)

        return quickSelect(0, len(nums) - 1)