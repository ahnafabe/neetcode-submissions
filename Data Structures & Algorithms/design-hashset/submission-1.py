class MyHashSet:

    def __init__(self):
        self.hashSet = []
        for i in range(10000):
            self.hashSet.append([])

    def add(self, key: int) -> None:
        index = key % 10000
        if key not in self.hashSet[index]:
            (self.hashSet[index]).append(key)

    def remove(self, key: int) -> None:
        index = key % 10000
        if key in self.hashSet[index]:
            (self.hashSet[index]).remove(key)

    def contains(self, key: int) -> bool:
        index = key % 10000
        if key in self.hashSet[index]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)