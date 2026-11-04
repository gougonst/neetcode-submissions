class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Sort hand
        # Sorted: [1, 2, 2, 3, 3, 4, 4, 5]
        # Create an array stores each group
        # For each distinct card, fill it from first to last group
        # If the difference between group[-1] and card is > 1 => False
        # If the group already satisfied group size, skip it.
        #   It must finised follow the order
        # If last group's size != group size => False

        if len(hand) % groupSize != 0:
            return False

        # Sort
        hand.sort()
        n = len(hand)

        groups = []
        finishedGroups = 0

        i = 0
        while i < n:
            j = i
            fillingGroup = finishedGroups
            while j < n and hand[j] == hand[i]:
                if fillingGroup >= len(groups):
                    groups.append([])

                group = groups[fillingGroup]
                if len(group) > 0 and hand[j] - group[-1] > 1:
                    return False

                group.append(hand[j])
                if len(group) == groupSize:
                    finishedGroups += 1

                fillingGroup += 1
                j += 1
            i = j

        return len(groups[-1]) == groupSize
    
        















                    