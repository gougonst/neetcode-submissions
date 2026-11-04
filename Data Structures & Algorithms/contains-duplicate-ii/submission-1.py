class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        nearbyChar = set()
        for i, num in enumerate(nums):
            if nums[i] in nearbyChar:
                return True

            if i >= k:
                nearbyChar.remove(nums[i - k])
            nearbyChar.add(nums[i])
        return False