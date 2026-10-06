class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        majority = size//2
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        for number in freq:
            if freq[number] > majority:
                return number