class Twitter:

    def __init__(self):
        self.followInfo = defaultdict(set)
        self.tweetInfo = defaultdict(list)
        self.nNewsFeed = 10
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetInfo[userId].append([self.timestamp, tweetId])
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []
        newsFeed = []

        self.followInfo[userId].add(userId)
        for followee in self.followInfo[userId]:
            if followee not in self.tweetInfo:
                continue
            timestamp = self.tweetInfo[followee][-1][0]
            tweetId = self.tweetInfo[followee][-1][1]
            heapq.heappush(pq, [-timestamp, tweetId, followee, len(self.tweetInfo[followee]) - 1])
        
        while pq and len(newsFeed) < 10:
            _, tweetId, followee, index = heapq.heappop(pq)
            newsFeed.append(tweetId)

            index -= 1
            if index >= 0:
                timestamp = self.tweetInfo[followee][index][0]
                tweetId = self.tweetInfo[followee][index][1]
                heapq.heappush(pq, [-timestamp, tweetId, followee, index])

        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followInfo[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followInfo[followerId]:
            self.followInfo[followerId].remove(followeeId)
