class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            
            # [Large (m), Small]
            if ((m + 1 < len(nums) and nums[m] > nums[m + 1])
                or (m > 0 and nums[m - 1] > nums[m])):
                if target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[r] < nums[m]:
                if (target < nums[m] 
                    and target >= nums[l]):
                    r = m - 1
                else:
                    l = m + 1
            else:
                if (target > nums[m]
                    and target <= nums[r]):
                    l = m + 1
                else:
                    r = m - 1
        return -1