class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l, r = 0, len(people) - 1
        numBoat = len(people)

        while l < r:
            maximum = people[l]
            minimum = people[r]
            remain = limit - maximum

            if remain >= minimum:
                r -= 1
                numBoat -= 1
            l += 1
        return numBoat