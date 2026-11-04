class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums: List[int], l: int, r: int) -> None:
        if l == r:
            return

        def merge(nums: List[int], l: int, m: int, r: int) -> None:
            left, right = nums[l:m + 1], nums[m + 1:r + 1]
            lIdx, rIdx, idx = 0, 0, l
            while lIdx < len(left) and rIdx < len(right):
                if left[lIdx] <= right[rIdx]:
                    nums[idx] = left[lIdx]
                    lIdx += 1
                else:
                    nums[idx] = right[rIdx]
                    rIdx += 1
                idx += 1
            
            while lIdx < len(left):
                nums[idx] = left[lIdx]
                idx += 1
                lIdx += 1
            
            while rIdx < len(right):
                nums[idx] = right[rIdx]
                idx += 1
                rIdx += 1

        m = l + (r - l) // 2
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m + 1, r)
        merge(nums, l, m, r)