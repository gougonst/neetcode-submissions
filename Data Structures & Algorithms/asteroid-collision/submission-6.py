class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        broken = set()

        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                continue
            j = i - 1
            while j >= 0 and (j in broken or asteroids[j] > 0):
                if j not in broken:
                    if asteroids[j] <= abs(asteroids[i]):
                        broken.add(j)
                    if asteroids[j] >= abs(asteroids[i]):
                        broken.add(i)
                        break
                j -= 1
        
        ans = []
        for i in range(len(asteroids)):
            if i not in broken:
                ans.append(asteroids[i])
        return ans