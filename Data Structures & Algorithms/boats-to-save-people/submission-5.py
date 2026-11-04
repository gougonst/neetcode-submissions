class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m + 1)
        for weight in people:
            count[weight] += 1

        i = len(people) - 1
        for weight, number in enumerate(count):
            for _ in range(number):
                people[i] = weight
                i -= 1

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