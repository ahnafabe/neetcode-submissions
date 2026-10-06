class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        my_list =[]
        for i in range(2):
            for num in nums:
                my_list.append(num)
        return my_list

        