class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant, dire = deque(), deque()
        for i, person in enumerate(senate):
            if person == "R":
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()
        return "Radiant" if radiant else "Dire"