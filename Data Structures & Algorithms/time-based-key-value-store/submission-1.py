class TimeMap:
    """
    Intuition:
    - Key, value => Hashmap or dict {}
    - dict stores list of tuple for timestamp and value.
    - Find the correct timestamp can use binary search.
    - Defaultdict to auto initilize key
    """

    def __init__(self):
        # create dict
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # find the appropriate key
        ans = self.timeMap[key]
        if not ans:
            return ""
        # found they key now find the timestamp
        else:
            # the correct timestamp can use binary search for it
            # luckily the problem insert the value increasing through time
            l, r = 0, len(ans) - 1
            value = ""
            while l <= r:
                mid = (r + l) // 2
                # yes the time is smaller than finding timestamp
                if ans[mid][0] <= timestamp:
                    value = ans[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
        return value
