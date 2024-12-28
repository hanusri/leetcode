from typing import List
import heapq

class Twitter:
    def __init__(self) -> None:
        self.tweets = {}
        self.followers = {}
        self.timestamp = 0
    
    def follow(self, followerId: int, followeeId: int):
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int):
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.timestamp, tweetId))
        if len(self.tweets[userId]) > 0:
            self.tweets[userId].pop(0)
    
    def getNewsFeed(self, userId: int) -> List[int]:
        # First all the followers of this users. Load first tweet from all followers into heap
        heap = []
        followees = self.followers.get(userId, set()) | {userId}
        for followee in followees:
            if followee in self.tweets and self.tweets[followee]:
                timestamp, tweetId = self.tweets[followee][-1]
                heap.append((-timestamp, tweetId, followee, len(self.tweets[followee])-1))
        feed = []
        heapq.heapify(heap)
        while len(heap) > 0 and len(feed) < 10:
            _, tweetId, followeeId, index = heapq.heappop(heap)
            feed.append(tweetId)
            if index > 0:
                next_timestamp, next_tweetId = self.tweets[followeeId][index - 1]
                heapq.heappush(heap, (-next_timestamp, next_tweetId, followeeId, index - 1))
        return feed

