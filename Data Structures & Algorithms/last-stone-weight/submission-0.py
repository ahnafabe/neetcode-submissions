class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      

        while len(stones) > 1:
            new_stone = 0
            x = max(stones)
            stones.remove(x)

            y = max(stones)
            stones.remove(y)

            if x < y:
                new_stone = y - x
                stones.append(new_stone)
            elif x > y:
                new_stone = x - y
                stones.append(new_stone)
        if len(stones) == 1:
            return stones[0]
        return 0