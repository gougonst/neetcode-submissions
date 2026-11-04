class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        labelCount = collections.Counter(s)

        ans = []

        seen = set()
        finished = set()
        lastEnd = -1
        for i, c in enumerate(s):
            seen.add(c)
            labelCount[c] -= 1
            if labelCount[c] == 0:
                finished.add(c)
            if finished == seen:
                ans.append(i - lastEnd)
                seen = set()
                finished = set()
                lastEnd = i
        return ans
        