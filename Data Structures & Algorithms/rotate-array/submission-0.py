class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return nums

        n = len(nums)
        steps = k % n

        count = 0
        start = 0

        while count < n:
            cur = start
            tmp = nums[cur]
            while True:
                next = (cur + steps) % n
                nums[next], tmp = tmp, nums[next]
                cur = next
                count += 1

                if cur == start:
                    break
            start += 1
                
        