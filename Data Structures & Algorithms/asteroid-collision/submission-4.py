class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue

            existFlag = True
            while stack and stack[-1] > 0:
                if stack[-1] > abs(asteroid):
                    existFlag = False
                    break
                elif stack[-1] == abs(asteroid):
                    existFlag = False
                    stack.pop()
                    break
                else:
                    stack.pop()

            if existFlag:
                stack.append(asteroid)

        return stack