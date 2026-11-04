class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        timeSlots = []
        for meeting in meetings:
            timeSlots.append(meeting[0])
            timeSlots.append(meeting[1])
        timeSlots.sort()
        availableRooms = [i for i in range(n)]
        usingMeetings = []

        bookedCount = Counter()
        i = 0
        for curTime in timeSlots:
            if i >= len(meetings):
                break

            start, end = meetings[i][0], meetings[i][1]
            interval = end - start

            # Release room from using meetings
            while usingMeetings and usingMeetings[0][0] <= curTime:
                _, _, roomId = heapq.heappop(usingMeetings)
                heapq.heappush(availableRooms, roomId)
            
            # Give meetings available rooms
            if start <= curTime and availableRooms:
                roomId = heapq.heappop(availableRooms)
                heapq.heappush(usingMeetings, (curTime + interval, curTime, roomId))
                bookedCount[roomId] += 1
                i += 1
        
        maxCount = max(bookedCount.values())
        candidates = []
        for roomId, count in bookedCount.items():
            if count == maxCount:
                candidates.append(roomId)
        return min(candidates)

