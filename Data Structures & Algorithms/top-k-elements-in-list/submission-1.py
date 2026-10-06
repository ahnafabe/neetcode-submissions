class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #loop through the array and store repeats into bins
        #then return k most frequent repeats
        
        freq_map = Counter(nums) #coiunt frequencies

        bucket = defaultdict(list) #create buckets (index = frequency)
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        result=[] #gather top k
        for freq in range(len(nums),0,-1):
            if freq in bucket:
                result.extend(bucket[freq])
            if len(result) >=k:
                return result[:k]