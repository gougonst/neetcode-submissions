class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # Find peak
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            
            mValue = mountainArr.get(m)
            prevValue = mountainArr.get(m - 1) if m > 0 else 0
            nextValue = mountainArr.get(m + 1) if m < n - 1 else 0
            if (prevValue < mValue and
                nextValue < mValue):
                peak = m
                break
            if (prevValue < mValue and
                nextValue > mValue):
                l = m + 1
            else:
                r = m - 1

        peakValue = mountainArr.get(peak)
        if target > peakValue:
            return -1
        
        # Find target in left part
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            mValue = mountainArr.get(m)
            if target == mValue:
                return m
            elif target > mValue:
                l = m + 1
            else:
                r = m - 1

        # Find target in right part
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) // 2
            mValue = mountainArr.get(m)
            if target == mValue:
                return m
            elif target < mValue:
                l = m + 1
            else:
                r = m - 1
        
        return -1

