class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sCount = {}
        tCount ={}
        
        for letter in s:
            if letter in sCount:
                sCount[letter]+= 1
            else:
                sCount[letter] = 1

        for letter in t:
            if letter in tCount:
                tCount[letter]+=1
            else:
                tCount[letter] = 1
        
        return sCount == tCount
        