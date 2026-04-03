class TimeMap:
    # using a dict of queue that contain the pair (timestamp, value)
    # now just loop through the queue and find correct ans

    def __init__(self):
        self.hash_map = defaultdict(deque)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # time stamp always go up so no need to sort
        self.hash_map[key].appendleft((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        q_res = self.hash_map[key]
        for obj in q_res:
            if timestamp >= obj[0]:
                return obj[1]
        return ""