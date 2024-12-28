class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hashKey = self._hash(key)
        for item in self.buckets[hashKey]:
            if item[0] == key:
                item[1] = value
                return
        self.buckets[hashKey].append([key, value])
        

    def get(self, key: int) -> int:
        hashKey = self._hash(key)
        for item in self.buckets[hashKey]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for i, item in enumerate(bucket):
            if item[0] == key:
                del bucket[i]
                return