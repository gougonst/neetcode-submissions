class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elementFreq = collections.defaultdict(int)

        for num in nums:
            elementFreq[num] += 1

            if len(elementFreq) <= 2:
                continue
                
            newElementFreq = collections.defaultdict(int)
            for element, freq in elementFreq.items():
                if freq > 1:
                    newElementFreq[element] = freq - 1
            elementFreq = newElementFreq
        
        criteria = len(nums) // 3

        res = set()
        realFreq = collections.defaultdict(int, { element: 0 for element in elementFreq })
        for num in nums:
            if num not in realFreq:
                continue
            realFreq[num] += 1
            if realFreq[num] > criteria:
                res.add(num)

        return list(res)