class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elementCount = collections.defaultdict(int)
        for num in nums:
            elementCount[num] += 1

        criteria = len(nums) // 3

        res = []
        for element, count in elementCount.items():
            if count > criteria:
                res.append(element)
        return res