class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrom(s:str) -> bool:
            string = s.lower()
            string = s.replace(" ","")
            string = "".join(c for c in s if c.isalnum())

            l = 0
            r = len(string) - 1

            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        isPalindrom(s)
        for char in s:
            if isPalindrom(s.replace(char,"")):
                return True
        return False