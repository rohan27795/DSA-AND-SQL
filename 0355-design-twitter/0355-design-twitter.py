class Twitter(object):

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        minheap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                count,tweetId = self.tweetMap[followeeId][index]
                minheap.append([count,tweetId,followeeId,index-1])
        heapq.heapify(minheap)

        while minheap and len(res) < 10:
            count,tweetId,followeeId,index = heapq.heappop(minheap)
            res.append(tweetId)

            if index>=0:
                count,tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minheap,[count,tweetId,followeeId,index-1])

        return res




        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)