class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = []
        numCount = Counter(nums)

        def permutation(cur: List[int]):
            if len(cur) == n:
                res.append(cur.copy())

            for num, count in numCount.items():
                if count <= 0:
                    continue
                cur.append(num)
                numCount[num] -= 1
                permutation(cur)
                cur.pop()
                numCount[num] += 1

        permutation([])
        return res