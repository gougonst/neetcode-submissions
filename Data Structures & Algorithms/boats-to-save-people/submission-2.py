class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        remains = []
        numBoat = 0

        for weight in people:
            remain = limit - weight
            
            if remains and -remains[0] >= weight:
                existBoat = -heapq.heappop(remains)
            else:
                if remain != 0:
                    heapq.heappush(remains, -remain)
                numBoat += 1
        
        return numBoat
