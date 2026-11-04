class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        stack = []
        radiant, dire = set(), set()
        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.add(i)
            else:
                dire.add(i)

        cur = 0
        while radiant and dire:
            if not stack or stack[-1] == senate[cur]:
                stack.append(senate[cur])
            else:
                if senate[cur] == "R":
                    radiant.remove(cur)
                else:
                    dire.remove(cur)
                stack.pop()

            cur = (cur + 1) % len(senate)
            while cur not in radiant and cur not in dire:
                cur = (cur + 1) % len(senate)

        return "Radiant" if radiant else "Dire"
            


# R D R D D R
# R R D D R
# R R D R
# R R D
# R R

# R D R D D R
# R D R D R
# R D D R
# R D D
# R D
# D