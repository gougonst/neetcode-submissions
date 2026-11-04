class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        fromStack, toStack = [], []
        for nPassengers, from_, to in trips:
            fromStack.append((from_, nPassengers))
            toStack.append((to, nPassengers))
        
        fromStack.sort(key=lambda x: x[0], reverse=True)
        toStack.sort(key=lambda x: x[0], reverse=True)

        curPassengers = 0
        while fromStack and toStack:
            fromDistance, fromPassengers = fromStack[-1]
            toDistance, toPassengers = toStack[-1]
            if fromDistance <= toDistance:
                curPassengers += fromPassengers
                fromStack.pop()
            if toDistance <= fromDistance:
                curPassengers -= toPassengers
                toStack.pop()
            if curPassengers > capacity:
                return False
        return True