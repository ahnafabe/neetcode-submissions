class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occurences = 0
        for number in nums:
            if number == val:
                occurences += 1


        k = len(nums) - occurences

        n = len(nums) # length of array
        i=0
        while i<n:
            if nums[i] == val: #if it is the value
                n-=1
                nums[i] = nums[n] # swap
            else:
                i+=1
        return k