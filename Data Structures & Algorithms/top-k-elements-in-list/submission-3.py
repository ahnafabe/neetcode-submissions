class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        output = []
        for num in nums:
            if num not in dict:
                dict[num] = 1
            dict[num] += 1 # at this point weve got a dic tracking the frequency of each number
        #[1,2,2,2,3,3] -> {1:1, 2:3, 3:2}

        while len(output) < k:
            max = 0
            idx = 0
            for key in dict:
                if dict[key] > max:
                    max = dict[key]
                    idx = key
            output.append(idx)
            del dict[idx]
        return output