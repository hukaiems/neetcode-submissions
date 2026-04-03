class TimeMap:
    # using a dict of queue that contain the pair (timestamp, value)
    # now just loop through the queue and find correct ans
    """
    O(log(N)) method
    """
    def __init__(self):
        self.hash_map = defaultdict(deque)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # time stamp always go up so no need to sort
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        q_res = self.hash_map[key]
        l, r = 0, len(q_res) - 1
        res = ""

        while l <= r:
            mid = (r + l) // 2
            if q_res[mid][0] == timestamp:
                return q_res[mid][1]
            elif q_res[mid][0] < timestamp:
                res = q_res[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res


    """
    O(N) method
    """
    # def __init__(self):
    #     self.hash_map = defaultdict(deque)

    # def set(self, key: str, value: str, timestamp: int) -> None:
    #     # time stamp always go up so no need to sort
    #     self.hash_map[key].appendleft((timestamp, value))

    # def get(self, key: str, timestamp: int) -> str:
    #     q_res = self.hash_map[key]
    #     for obj in q_res:
    #         if timestamp >= obj[0]:
    #             return obj[1]
    #     return ""