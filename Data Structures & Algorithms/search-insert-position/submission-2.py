class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #     elif nums[len(nums)-1] < target:
        #         return len(nums)
        #     elif nums[0] > target:
        #         return 0
        #     elif nums[i] < target and nums[i+1] > target:
        #         return i+1
        res = len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res