class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #loop thorugh array
        #remove element from array
        #multiply conternts of array and append to result list 

        result = []
    
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]  
            product = 1
            for num in temp:
                product *= num  
            result.append(product)
    
        return result
        