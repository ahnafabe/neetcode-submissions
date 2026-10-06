class Solution:
    def isPalindrome(self, s: str) -> bool:
        #get rid of all spaces
        #load into an array
        #then push each element from array into stack
        #if both array and stack same then true

        # cleaned = []
        # for letter in s:
        #     if letter.isalnum():# check alphanumeric
        #         cleaned.append(letter.lower()) #lowercase each letter 
        # stack = []
        # for letter in cleaned:
        #     stack.append(letter)

        # for letter in cleaned:
        #     if letter!= stack.pop(): # pops and returns last element
        #         return False

        # return True
        # Above implementation is o(n), can we do better?

        #########################################################
        # Alternate implementation
        # load cleaned string into an array
        # compare first element with last element, then increment each pointer towards each other

        cleaned = []
        for letter in s:
            if letter.isalnum():
                cleaned.append(letter.lower())
        # Compare forward vs backward
        for i in range(len(cleaned) // 2):  # Only need to check half
            if cleaned[i] != cleaned[-i - 1]:  # -i-1 gets mirror position
                return False
        return True
        