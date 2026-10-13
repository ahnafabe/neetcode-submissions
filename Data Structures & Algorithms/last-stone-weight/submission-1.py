class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            new_stone = 0
            x = heapq.heappop(stones)
            x = x * -1

            y = heapq.heappop(stones)
            y = y * -1

            if x < y:
                new_stone = y - x
                new_stone = new_stone * -1
                heapq.heappush(stones, new_stone)
            elif x > y:
                new_stone = x - y
                new_stone = new_stone * -1
                heapq.heappush(stones, new_stone)
        if len(stones) == 1:
            return stones[0] * -1
        return 0  


