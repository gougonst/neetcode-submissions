class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        possible = [False] * 3

        for triplet in triplets:
            tripletPossible = [False] * 3
            validFlag = True
            for i in range(3):
                if triplet[i] > target[i]:
                    validFlag = False
                elif triplet[i] == target[i]:
                    tripletPossible[i] = True
            if not validFlag:
                continue
            possible = [possible[i] or tripletPossible[i] for i in range(3)]
        return all(possible)
            