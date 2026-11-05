class Twitter:

    MAX_MOST_RECENT_TWEETS = 10

    def __init__(self):
        self.posts = {}
        self.follows = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts: self.posts[userId] = []
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = [self._get_posts(followeeId) for followeeId in self._get_follows(userId)]
        max_indices = [len(posts[i]) for i in range(len(posts))]
        indices = [len(post) - 1 for post in posts]
        # Merge n sorted arrays
        res = []
        n_added = 0
        while True:
            # Select minimum time post
            max_time = -1
            max_time_index = None
            max_time_tweetId = None
            for i in range(len(posts)):
                post = posts[i]
                if indices[i] >= 0:
                    time, tweetId = post[indices[i]]
                    if time > max_time:
                        max_time = time
                        max_time_index = i
                        max_time_tweetId = tweetId
            
            if max_time_index is None:
                break  # no more to add
            res.append(max_time_tweetId)
            indices[max_time_index] -= 1
            n_added += 1
            if n_added >= Twitter.MAX_MOST_RECENT_TWEETS:
                break
        return res

    def _get_posts(self, userId) -> List(int):
        if userId not in self.posts: return []
        return self.posts[userId]

    def _get_follows(self, userId) -> set(int):
        if userId not in self.follows: return {userId}
        return self.follows[userId].union({userId})

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
