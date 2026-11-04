class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        availableRooms = [i for i in range(n)]
        usingMeetings = []

        bookedCount = [0] * n
        for meeting in meetings:
            start, end = meeting
            interval = end - start

            # Release rooms from using meetings
            while usingMeetings and usingMeetings[0][0] <= start:
                _, roomId = heapq.heappop(usingMeetings)
                heapq.heappush(availableRooms, roomId)
            
            # Give meeting available room
            if availableRooms:
                roomId = heapq.heappop(availableRooms)
                heapq.heappush(usingMeetings, (start + interval, roomId))
            else:
                readyTime, roomId = heapq.heappop(usingMeetings)
                heapq.heappush(usingMeetings, (readyTime + interval, roomId))

            bookedCount[roomId] += 1
        
        return bookedCount.index(max(bookedCount))

