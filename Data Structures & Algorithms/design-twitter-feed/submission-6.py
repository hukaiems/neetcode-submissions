"""
Lesson:
- Appending a list into a list, use += to append element, append for append the whole list [[]].
"""

"2 hashes and a max heap"
class Twitter:

    def __init__(self):
        # a hash of userId and their newFeed, a set to store followerId.
        self.hash_feed = defaultdict(list)
        self.follower_set = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # append the tweet into hash_feed of that user
        self.time -= 1
        time = self.time
        self.hash_feed[userId].append([time, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        new_feed = []

        # first append the new_feed of user
        new_feed += self.hash_feed[userId]

        # Second append the new_feed of followee
        for followeeId in self.follower_set[userId]:
            new_feed += self.hash_feed[followeeId]
        
        # now heapify and return
        heapq.heapify(new_feed)
        res = []

        while new_feed and len(res) < 10:
            res.append(heapq.heappop(new_feed)[1])

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        # add followeeId into the set
        if followerId != followeeId:
            self.follower_set[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove from the set
        if followeeId in self.follower_set[followerId]:
            self.follower_set[followerId].remove(followeeId)

# Time: O(N) for the heapify
# Space: O(N) for the heap