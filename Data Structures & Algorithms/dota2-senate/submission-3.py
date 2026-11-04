class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = deque([]), deque([])
        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r > d:
                dire.append(d + len(senate))
            else:
                radiant.append(r + len(senate))
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