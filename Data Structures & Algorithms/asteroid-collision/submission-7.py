class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remain = []

        for cur in asteroids:
            if cur > 0:
                remain.append(cur)
                continue

            isBroke = False
            while remain and remain[-1] > 0 and not isBroke:
                opponent = remain[-1]
                if abs(cur) >= opponent:
                    remain.pop()
                if abs(cur) <= opponent:
                    isBroke = True
            if not isBroke:
                remain.append(cur)

        return remain