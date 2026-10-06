class MyHashMap:
    #Currently we have init make a list that has 10000 elements, the value of each element is a list
    def __init__(self):
        self.hashmap = []
        for i in range(10000):
            self.hashmap.append([]) 
    
    def put(self, key: int, value: int) -> None:
        index = key % 10000
        for pair in self.hashmap[index]:
            if pair[0] == key:
                pair[1] = value  # Update
                return
    # Key not found, append new pair
        self.hashmap[index].append([key, value])

    def get(self, key: int) -> int:
        index = key % 10000
        if len(self.hashmap[index])>0:
            for pair in self.hashmap[index]:
                if pair[0] == key:
                    val = pair[1]
                    return val
        return -1
        

    def remove(self, key: int) -> None:
        index = key % 10000
        for pair in self.hashmap[index]:
            if pair[0] == key:
                self.hashmap[index].remove(pair)
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)