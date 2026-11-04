class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cardCount = collections.defaultdict(int)
        for card in hand:
            cardCount[card] += 1

        cards = list(cardCount.keys())
        heapq.heapify(cards)

        while cards:
            minCard = heapq.heappop(cards)
            count = cardCount[minCard]
            if count == 0:
                continue
            for i in range(groupSize):
                cardCount[minCard + i] -= count
                if cardCount[minCard + i] < 0:
                    return False
            
        return True
    
        















                    