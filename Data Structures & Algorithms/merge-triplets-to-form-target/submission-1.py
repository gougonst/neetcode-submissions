class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        possible = 0b000

        for triplet in triplets:
            tripletPossible = 0b000
            validFlag = True
            for i in range(3):
                if triplet[i] > target[i]:
                    validFlag = False
                elif triplet[i] == target[i]:
                    tripletPossible |= (1 << i)
            if not validFlag:
                continue
            possible |= tripletPossible
        return possible == 0b111
            