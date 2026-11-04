class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def dryRun(capacity: int) -> bool:
            curCapacity = 0
            curDay = 1
            for i in range(len(weights)):
                curCapacity += weights[i]
                if curCapacity > capacity:
                    curDay += 1
                    curCapacity = weights[i]
                if curDay > days:
                    return False
            return True

        l, r = max(weights), sum(weights)
        while l < r:
            m = l + (r - l) // 2
            if dryRun(m):
                r = m
            else:
                l = m + 1
        return r

