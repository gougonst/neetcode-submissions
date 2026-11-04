class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []
        for nPassengers, from_, to in trips:
            points.append((from_, nPassengers))
            points.append((to, -nPassengers))
        points.sort()

        curPassengers = 0
        for _, passengers in points:
            curPassengers += passengers
            if curPassengers > capacity:
                return False
        return True