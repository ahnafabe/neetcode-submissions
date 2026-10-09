class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can put in a hash map to count letters and if same. then true

        freqS = {}
        for letter in s:
            if letter not in freqS:
                freqS[letter] = 1
            else:
                freqS[letter] +=1
        
        freqT = {}
        for letter in t:
            if letter not in freqT:
                freqT[letter] =1
            else:
                freqT[letter] +=1
        
        if freqT == freqS:
            return True
        else:
            return False