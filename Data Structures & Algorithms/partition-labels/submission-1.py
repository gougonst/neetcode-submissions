class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        ans = []
        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, lastIndex[c])

            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        return ans
        