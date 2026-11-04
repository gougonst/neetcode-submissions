class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums[0]

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        duplicate = 0
        while True:
            slow = nums[slow]
            duplicate = nums[duplicate]
            if slow == duplicate:
                return duplicate
        